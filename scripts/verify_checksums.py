#!/usr/bin/env python3
"""Verify SHA256SUMS.txt for the public LangWarrant artifact."""
from __future__ import annotations
import argparse, hashlib
from pathlib import Path

def sha256_file(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo-root', default='.')
    ap.add_argument('--sha-file', default='SHA256SUMS.txt')
    args=ap.parse_args()
    root=Path(args.repo_root)
    ok=0; bad=0; missing=0
    for line in (root/args.sha_file).read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        digest, rel = line.split(None, 1)
        rel=rel.strip().lstrip('*')
        p=root/rel
        if not p.exists():
            print(f'MISSING {rel}'); missing+=1; continue
        got=sha256_file(p)
        if got!=digest:
            print(f'BAD {rel}: expected {digest}, got {got}'); bad+=1
        else: ok+=1
    print(f'OK={ok} BAD={bad} MISSING={missing}')
    raise SystemExit(1 if bad or missing else 0)
if __name__ == '__main__': main()
