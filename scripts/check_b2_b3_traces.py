# -*- coding: utf-8 -*-
import os, json
from inspect_traces_detail import extract_plotly_data, BASE_DIR

for fname in ["B2_17.html", "B2_18.html", "B2_19.html", "B2_22.html", "B3_1.html", "B3_4.html", "B3_11.html", "B3_14.html"]:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    data = extract_plotly_data(text)
    print(f"=== {fname} ===")
    for idx, t in enumerate(data):
        ttype = t.get('type')
        if ttype in ['surface', 'mesh3d', 'scatter']:
            print(f"  [{idx}] {ttype} name={t.get('name')} opacity={t.get('opacity')} scene={t.get('scene')}")
