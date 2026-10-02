# -*- coding: utf-8 -*-
import os, json, glob
from inspect_traces_detail import extract_plotly_data, BASE_DIR

for prefix in ["B1", "B2"]:
    n_max = 20 if prefix == "B1" else 22
    for i in range(1, n_max + 1):
        fname = f"{prefix}_{i}.html"
        fpath = os.path.join(BASE_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
        data = extract_plotly_data(text)
        names = [f"{t.get('type')}({t.get('name')})" for t in data] if data else []
        print(f"{fname}: {', '.join(names)}")
