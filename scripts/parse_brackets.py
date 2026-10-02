# -*- coding: utf-8 -*-
import os, json

filepath = r'C:\Users\khải\.gemini\antigravity\scratch\TCC3\B3_11.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("Plotly.newPlot(")
if idx != -1:
    # find first comma
    comma_idx = text.find(",", idx)
    # find first [
    bracket_idx = text.find("[", comma_idx)
    
    # parse until matching ]
    count = 0
    end_idx = -1
    in_string = False
    escape = False
    for i in range(bracket_idx, len(text)):
        char = text[i]
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
        elif char == '"':
            in_string = not in_string
        elif not in_string:
            if char == '[': count += 1
            elif char == ']': count -= 1
            
            if count == 0:
                end_idx = i
                break
                
    if end_idx != -1:
        data_str = text[bracket_idx:end_idx+1]
        try:
            data = json.loads(data_str)
            print("Successfully loaded JSON! Length:", len(data))
            for i, t in enumerate(data):
                print(f"Trace {i}: type={t.get('type')}, name={t.get('name')}")
        except Exception as e:
            print("Error parsing:", e)
else:
    print("Plotly.newPlot not found")
