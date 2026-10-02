# -*- coding: utf-8 -*-
import os, re, json
import numpy as np

filepath = r'C:\Users\khải\.gemini\antigravity\scratch\TCC3\B3_11.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Find the Plotly.newPlot call
# The data array starts after the first comma.
match = re.search(r"Plotly\.newPlot\(\s*'[^']+',\s*(\[\{.*?\}\]),\s*\{", text, flags=re.DOTALL)
if match:
    data_str = match.group(1)
    try:
        data = json.loads(data_str)
        print("Successfully loaded JSON!")
        print("Traces:", len(data))
        for i, t in enumerate(data):
            print(f"Trace {i}: type={t.get('type')}, name={t.get('name')}")
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
else:
    print("Pattern not found!")
