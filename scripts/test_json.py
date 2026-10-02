# -*- coding: utf-8 -*-
import os, re, json

filepath = r'C:\Users\khải\.gemini\antigravity\scratch\TCC3\B3_11.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Plotly format: {"data":[{"type":"surface",...}],"layout":{...}}
match = re.search(r'"data":(\[\{"type".*?\}\]),"layout":', text)
if match:
    # Let's extract exactly the data array
    data_str = match.group(1)
    print("Found data array of length:", len(data_str))
else:
    print('Pattern not found!')
