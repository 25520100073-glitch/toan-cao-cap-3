# -*- coding: utf-8 -*-
import os, json
import numpy as np

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

def extract_plotly_data(text):
    idx = text.find("Plotly.newPlot(")
    if idx == -1: return None
    comma_idx = text.find(",", idx)
    bracket_idx = text.find("[", comma_idx)
    count = 0
    in_string = False
    escape = False
    for i in range(bracket_idx, len(text)):
        ch = text[i]
        if escape:
            escape = False
            continue
        if ch == '\\': escape = True
        elif ch == '"': in_string = not in_string
        elif not in_string:
            if ch == '[': count += 1
            elif ch == ']': count -= 1
            if count == 0:
                return json.loads(text[bracket_idx:i+1])
    return None

for fname in ["B2_17.html", "B2_18.html", "B2_19.html", "B2_22.html"] + [f"B3_{i}.html" for i in range(1, 16)]:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    data = extract_plotly_data(text)
    print(f"=== {fname} ===")
    for idx, t in enumerate(data):
        ttype = t.get('type')
        if ttype in ['surface', 'mesh3d', 'scatter']:
            print(f"  [{idx}] {ttype} name={t.get('name')} color={t.get('colorscale') or t.get('color') or t.get('line')}")
        elif ttype == 'scatter3d' and t.get('mode') == 'lines':
            # check if it's axis or boundary line
            x = t.get('x', [])
            print(f"  [{idx}] scatter3d(lines) len={len(x)} color={t.get('line', {}).get('color')}")
