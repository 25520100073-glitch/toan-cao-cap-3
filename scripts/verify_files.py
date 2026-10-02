# -*- coding: utf-8 -*-
import os, glob

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

for prefix, count in [('B1', 20), ('B2', 22)]:
    print(f"=== Kiểm tra {prefix} ===")
    missing_plots = []
    missing_sols = []
    for i in range(1, count + 1):
        path = os.path.join(BASE_DIR, f"{prefix}_{i}.html")
        if not os.path.exists(path):
            print(f"Missing file: {prefix}_{i}.html")
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            if 'Plotly.newPlot' not in content and 'plotly-graph-div' not in content:
                missing_plots.append(i)
            if 'Lời giải' not in content:
                missing_sols.append(i)
    
    print(f"{prefix} files missing plots: {missing_plots}")
    print(f"{prefix} files missing solutions: {missing_sols}")
