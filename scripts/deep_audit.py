# -*- coding: utf-8 -*-
import os, re, glob

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

def deep_audit():
    files = sorted(glob.glob(os.path.join(BASE_DIR, "B*.html")))
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # Remove the huge plotly script blocks to inspect visible HTML
        # Plotly script starts with <script type="text/javascript"> or <script>/**
        # Let's just strip everything between <div class="plot-container"> and the closing </div></div> of plot-container
        p_start = text.find('<div class="plot-container">')
        if p_start != -1:
            # Find where the plot container ends
            # In B1/B2/B3, after plot-container is either <h3>Mã Nguồn or <div style="background:#eaf4fb
            p_end = text.find('</script>', p_start)
            while p_end != -1:
                next_script = text.find('<script', p_end + 9)
                if next_script != -1 and next_script - p_end < 200:
                    p_end = text.find('</script>', next_script)
                else:
                    break
            if p_end != -1:
                visible = text[:p_start] + text[p_end+9:]
            else:
                visible = text[:p_start]
        else:
            visible = text
            
        # 1. Check for $...$ inline math
        dollars = re.findall(r'(?<!\\)\$[^\$]+(?<!\\)\$', visible)
        if dollars:
            print(f"[MATH $] {fname}: {len(dollars)} instances of $...$ (e.g. {dollars[:2]})")
            
        # 2. Check for mojibake / replacement char \ufffd
        if '\ufffd' in visible:
            print(f"[ENCODING] {fname}: Contains \\ufffd replacement char!")
            
        # 3. Check for unrendered LaTeX commands outside math delimiters or broken delimiters
        if 'Cảnh báo' in visible or 'Đang chờ' in visible:
            print(f"[WARNING BOX] {fname}: Still has warning/placeholder box!")
            
        # 4. Check if solution exists
        if 'Lời giải' not in visible:
            print(f"[NO SOLUTION] {fname}: Missing Lời giải!")

if __name__ == "__main__":
    deep_audit()
    print("Audit complete.")
