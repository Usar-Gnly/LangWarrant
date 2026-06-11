#!/usr/bin/env python3
"""Recompute LW3 analysis tables from the public LangWarrant artifact.

Usage:
  python scripts/compute_lw3_analysis_tables.py --repo-root .
"""
from __future__ import annotations
import argparse, ast, json, math, os
from pathlib import Path
import pandas as pd

OFFICIAL_RUNS=['openai_gpt55_main_v1','google_gemini35flash_main_v1','anthropic_sonnet46_main_v1','qwen3_8b_main_v1','aya_expanse_8b_main_v1','llama31_8b_main_v1']
MODEL_ORDER=['GPT-5.5','Gemini 3.5 Flash','Claude Sonnet 4.6','Qwen3-8B-Instruct','Aya Expanse 8B','Llama-3.1-8B-Instruct']

def wilson(k,n,z=1.96):
    if n==0: return (float('nan'), float('nan'))
    p=k/n; denom=1+z*z/n
    center=(p+z*z/(2*n))/denom
    half=z*math.sqrt((p*(1-p)+z*z/(4*n))/n)/denom
    return center-half, center+half

def source_family(s):
    return {
        'explicit_user_instruction':'Explicit instruction',
        'customer_response_locale':'Customer response locale',
        'policy_selected_contact_locale':'Policy-selected contact locale',
        'active_outbound_surface':'Active outbound surface',
        'schema_visible_locale_policy':'Schema-visible locale policy',
    }.get(s,'Other field-level locale')

def normalize_slice(x):
    if isinstance(x,list): return x
    if isinstance(x,str):
        try:
            y=ast.literal_eval(x)
            if isinstance(y,list): return y
        except Exception:
            return [x]
    return []

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo-root', default='.', help='Repository root containing data/ and results/.')
    ap.add_argument('--out-dir', default='results/lw3_analysis_recomputed')
    args=ap.parse_args()
    root=Path(args.repo_root)
    metrics_root=root/'results/scored_runs'
    data_path=root/'data/frozen_release/SLD_Bench_v1_0_Full1500_all_1500rows.jsonl'
    out=root/args.out_dir; out.mkdir(parents=True, exist_ok=True)

    item_frames=[]; triad_frames=[]
    for run in OFFICIAL_RUNS:
        item_frames.append(pd.read_json(metrics_root/run/'item_scores.jsonl', lines=True))
        triad_frames.append(pd.read_json(metrics_root/run/'triad_scores.jsonl', lines=True))
    items=pd.concat(item_frames, ignore_index=True)
    triads=pd.concat(triad_frames, ignore_index=True)
    items['model_name']=pd.Categorical(items['model_name'], MODEL_ORDER, ordered=True)
    triads['model_name']=pd.Categorical(triads['model_name'], MODEL_ORDER, ordered=True)

    rows=[]
    for model in MODEL_ORDER:
        d=items[items.model_name==model]; g=triads[triads.model_name==model]
        lk=int(d.language_score.sum()); ln=len(d)
        tk=int(g.triad_warrant_consistency_score.sum()); tn=len(g)
        lci=wilson(lk,ln); tci=wilson(tk,tn)
        rows.append(dict(Model=model, LWA=lk/ln, LWA_lo=lci[0], LWA_hi=lci[1], TWCS=tk/tn, TWCS_lo=tci[0], TWCS_hi=tci[1], n_items=ln, n_groups=tn))
    pd.DataFrame(rows).to_csv(out/'headline_wilson_ci.csv', index=False)

    role=items.groupby(['model_name','group_role'], observed=True)['language_score'].mean().unstack()
    rel=triads.groupby('model_name', observed=True)[['warrant_shift_success','distractor_invariance_success','triad_warrant_consistency_score']].mean()
    role.join(rel).reset_index().to_csv(out/'role_counterfactual_diagnostics.csv', index=False)

    data=pd.read_json(data_path, lines=True)
    data['source_family']=data['target_language_source'].map(source_family)
    items['source_family']=items['target_language_source'].map(source_family)
    source_n=data.groupby('source_family').size().rename('Items')
    source_metrics=items.groupby('source_family')[['language_score','valid_response_score','task_completion_score','format_score','field_policy_score']].mean().join(source_n).reset_index()
    source_metrics.to_csv(out/'warrant_source_metrics.csv', index=False)

    shortcut_rows=[]
    for cue_col, name in [('operator_language','Follow operator language'),('material_language','Follow source/material language'),('audience_language','Follow audience language')]:
        valid=data[cue_col].notna()
        shortcut_rows.append(dict(Baseline=name, Items=int(valid.sum()), LWA=(data.loc[valid,cue_col]==data.loc[valid,'target_response_language']).mean()))
    majority=data['target_response_language'].value_counts().idxmax()
    shortcut_rows.append(dict(Baseline=f'Always majority target ({majority})', Items=len(data), LWA=(data['target_response_language']==majority).mean()))
    pd.DataFrame(shortcut_rows).to_csv(out/'shortcut_cue_baselines.csv', index=False)

    selected_tags={'conflicting_non_warrant_cues','audience_target_mismatch','operator_target_mismatch','material_target_mismatch','audience_target_match','operator_target_match','material_target_match','policy_pointer','active_surface','structured_output_field_policy','new300_vendor_procurement_logistics'}
    item_tags=[]
    for _, row in items.iterrows():
        for tag in normalize_slice(row['shortcut_slice']):
            if tag in selected_tags:
                item_tags.append({'tag':tag,'language_score':row['language_score'],'valid_response_score':row['valid_response_score']})
    data_tags=[]
    for _, row in data.iterrows():
        for tag in normalize_slice(row['shortcut_slice']):
            if tag in selected_tags: data_tags.append({'tag':tag})
    tag_df=pd.DataFrame(item_tags); data_tag_df=pd.DataFrame(data_tags)
    tag_metrics=tag_df.groupby('tag')[['language_score','valid_response_score']].mean().join(data_tag_df.groupby('tag').size().rename('Items')).reset_index().sort_values('Items', ascending=False)
    tag_metrics.to_csv(out/'shortcut_tag_metrics.csv', index=False)
    print(f'Wrote analysis tables to {out}')

if __name__ == '__main__':
    main()
