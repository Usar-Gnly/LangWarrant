import json, os, glob, math, ast
import pandas as pd
from collections import Counter, defaultdict

metrics_root='[LOCAL_BUILD_PATH_REMOVED]/lw3_metrics/SLD_Bench_04_FINAL_METRICS_FREEZE_APPROVED_v0_2k_2026-06-10/02_FINAL_RUN_METRICS/runs_v0_2k_recomputed_FINAL'
data_path='[LOCAL_BUILD_PATH_REMOVED]/resource_full/SLD_Bench_PAPER_WRITING_RESOURCE_BUNDLE_SLD11_2026-06-11/01_DATA_AND_DATASET/SLD_Bench_PAPER_01_DATA_ASSETS_v0_2k_FINAL_2026-06-10/01_FROZEN_DATASET_RELEASE/extracted_core_files/SLD_Bench_v1_0_Full1500_all_1500rows.jsonl'
official_runs=['openai_gpt55_main_v1','google_gemini35flash_main_v1','anthropic_sonnet46_main_v1','qwen3_8b_main_v1','aya_expanse_8b_main_v1','llama31_8b_main_v1']
run_order=official_runs
name_short={'GPT-5.5':'GPT-5.5','Gemini 3.5 Flash':'Gemini','Claude Sonnet 4.6':'Claude','Qwen3-8B-Instruct':'Qwen3','Aya Expanse 8B':'Aya','Llama-3.1-8B-Instruct':'Llama'}
model_order=['GPT-5.5','Gemini 3.5 Flash','Claude Sonnet 4.6','Qwen3-8B-Instruct','Aya Expanse 8B','Llama-3.1-8B-Instruct']

def wilson(k,n,z=1.96):
    if n==0: return (float('nan'), float('nan'))
    p=k/n
    denom=1+z*z/n
    center=(p+z*z/(2*n))/denom
    half=z*math.sqrt((p*(1-p)+z*z/(4*n))/n)/denom
    return center-half, center+half

items=[]; triads=[]
for run in official_runs:
    idf=pd.read_json(os.path.join(metrics_root,run,'item_scores.jsonl'), lines=True)
    tdf=pd.read_json(os.path.join(metrics_root,run,'triad_scores.jsonl'), lines=True)
    items.append(idf); triads.append(tdf)
items=pd.concat(items, ignore_index=True)
triads=pd.concat(triads, ignore_index=True)
# ensure order
items['model_name']=pd.Categorical(items['model_name'], model_order, ordered=True)
triads['model_name']=pd.Categorical(triads['model_name'], model_order, ordered=True)

# headline with Wilson
rows=[]
for model in model_order:
    d=items[items.model_name==model]
    g=triads[triads.model_name==model]
    lk=int(d.language_score.sum()); ln=len(d)
    tk=int(g.triad_warrant_consistency_score.sum()); tn=len(g)
    lci=wilson(lk,ln); tci=wilson(tk,tn)
    rows.append(dict(Model=model, LWA=lk/ln, LWA_lo=lci[0], LWA_hi=lci[1], TWCS=tk/tn, TWCS_lo=tci[0], TWCS_hi=tci[1], n_items=ln, n_groups=tn))
headline=pd.DataFrame(rows)

# role diagnostics
role=items.groupby(['model_name','group_role'], observed=True)['language_score'].mean().unstack()
# triad relation WSS DIS
rel=triads.groupby('model_name', observed=True)[['warrant_shift_success','distractor_invariance_success','triad_warrant_consistency_score']].mean()
role_table=role.join(rel).reset_index()

# source family mapping
def source_family(s):
    if s=='explicit_user_instruction': return 'Explicit instruction'
    if s=='customer_response_locale': return 'Customer response locale'
    if s=='policy_selected_contact_locale': return 'Policy-selected contact locale'
    if s=='active_outbound_surface': return 'Active outbound surface'
    if s=='schema_visible_locale_policy': return 'Schema-visible locale policy'
    return 'Other field-level locale'
items['source_family']=items['target_language_source'].map(source_family)
# item count per dataset, not per run
data=pd.read_json(data_path, lines=True)
data['source_family']=data['target_language_source'].map(source_family)
source_n=data.groupby('source_family').size().rename('Items')
source_metrics=items.groupby('source_family')[['language_score','valid_response_score','task_completion_score','format_score','field_policy_score']].mean().join(source_n).reset_index()
source_metrics=source_metrics[['source_family','Items','language_score','valid_response_score','task_completion_score','format_score','field_policy_score']]
source_order=['Explicit instruction','Customer response locale','Policy-selected contact locale','Active outbound surface','Schema-visible locale policy','Other field-level locale']
source_metrics['source_family']=pd.Categorical(source_metrics['source_family'],source_order,ordered=True)
source_metrics=source_metrics.sort_values('source_family')

# shortcut cue baseline from dataset
# compare fixed language cue to gold target
data['majority_lang']='en' # placeholder maybe actual majority
lang_counts=data['target_response_language'].value_counts()
majority=lang_counts.idxmax()
shortcut_rows=[]
for cue_col, name in [('operator_language','Follow operator language'),('material_language','Follow source/material language'),('audience_language','Follow audience language')]:
    valid=data[cue_col].notna()
    acc=(data.loc[valid,cue_col]==data.loc[valid,'target_response_language']).mean()
    shortcut_rows.append(dict(Baseline=name, Items=int(valid.sum()), LWA=acc))
shortcut_rows.append(dict(Baseline=f'Always majority target ({majority})', Items=len(data), LWA=(data['target_response_language']==majority).mean()))
# direct instruction oracle only where visible direct language instruction present; but limited subset not baseline across all
shortcut=pd.DataFrame(shortcut_rows)

# shortcut slice analysis: major tags from item shortcut_slice lists
# explode tags, compute LWA mean over official item-run rows and dataset count per tag

def normalize_slice(x):
    if isinstance(x,list): return x
    if isinstance(x,str):
        try:
            y=ast.literal_eval(x)
            if isinstance(y,list): return y
        except Exception:
            return [x]
    return []
item_tags=[]
for idx,row in items.iterrows():
    for tag in normalize_slice(row['shortcut_slice']):
        if tag in {'conflicting_non_warrant_cues','audience_target_mismatch','operator_target_mismatch','material_target_mismatch','audience_target_match','operator_target_match','material_target_match','policy_pointer','active_surface','structured_output_field_policy','new300_vendor_procurement_logistics'}:
            item_tags.append({'tag':tag,'language_score':row['language_score'],'valid_response_score':row['valid_response_score']})
tag_df=pd.DataFrame(item_tags)
data_tags=[]
for idx,row in data.iterrows():
    for tag in normalize_slice(row['shortcut_slice']):
        if tag in {'conflicting_non_warrant_cues','audience_target_mismatch','operator_target_mismatch','material_target_mismatch','audience_target_match','operator_target_match','material_target_match','policy_pointer','active_surface','structured_output_field_policy','new300_vendor_procurement_logistics'}:
            data_tags.append({'tag':tag})
data_tag_df=pd.DataFrame(data_tags)
tag_metrics=tag_df.groupby('tag')[['language_score','valid_response_score']].mean().join(data_tag_df.groupby('tag').size().rename('Items')).reset_index().sort_values('Items',ascending=False)

# role by source? maybe not

# Save CSVs
out='[LOCAL_BUILD_PATH_REMOVED]/lw3_analysis_outputs'; os.makedirs(out, exist_ok=True)
headline.to_csv(f'{out}/headline_wilson_ci.csv',index=False)
role_table.to_csv(f'{out}/role_counterfactual_diagnostics.csv',index=False)
source_metrics.to_csv(f'{out}/warrant_source_metrics.csv',index=False)
shortcut.to_csv(f'{out}/shortcut_cue_baselines.csv',index=False)
tag_metrics.to_csv(f'{out}/shortcut_tag_metrics.csv',index=False)

print('HEADLINE')
print(headline.to_string(index=False, float_format=lambda x:f'{x:.3f}'))
print('\nROLE')
print(role_table.to_string(index=False, float_format=lambda x:f'{x:.3f}'))
print('\nSOURCE')
print(source_metrics.to_string(index=False, float_format=lambda x:f'{x:.3f}'))
print('\nSHORTCUT')
print(shortcut.to_string(index=False, float_format=lambda x:f'{x:.3f}'))
print('\nTAGS')
print(tag_metrics.head(20).to_string(index=False, float_format=lambda x:f'{x:.3f}'))
