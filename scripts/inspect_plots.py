# -*- coding: utf-8 -*-
import os, re, glob, json

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

def inspect_b3_and_special_b2():
    targets = ["B2_17.html", "B2_18.html", "B2_19.html", "B2_22.html"] + [f"B3_{i}.html" for i in range(1, 16)]
    for fname in targets:
        fpath = os.path.join(BASE_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # get de bai
        m = re.search(r'<strong>Đề bài:</strong>(.*?)</(?:p|div)>', text, re.DOTALL)
        debai = m.group(1).strip() if m else "N/A"
        
        data = extract_plotly_data(text)
        trace_info = []
        if data:
            for idx, t in enumerate(data):
                ttype = t.get('type')
                tname = t.get('name', '')
                if ttype in ['surface', 'mesh3d']:
                    trace_info.append(f"{ttype}({tname})")
                elif ttype == 'scatter':
                    trace_info.append(f"2D:{tname}")
        print(f"{fname}: {debai}")
        print(f"   Traces: {', '.join(trace_info)}")

if __name__ == "__main__":
    inspect_b3_and_special_b2()
