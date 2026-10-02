# -*- coding: utf-8 -*-
import os, re, glob, json

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

def check_everything():
    files = sorted(glob.glob(os.path.join(BASE_DIR, "B*.html")))
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
            
        p_start = text.find('<div class="plot-container">')
        p_end = text.rfind('</script>')
        visible = text[:p_start] + (text[p_end+9:] if p_end != -1 else "")
        
        # Check if visible text after removing \(...\) and \[...\] and $$...$$ still has backslash commands
        cleaned = re.sub(r'\\\(.*?\\\)', '', visible, flags=re.DOTALL)
        cleaned = re.sub(r'\\\[.*?\\\]', '', cleaned, flags=re.DOTALL)
        # remove <pre class="code-block">...</pre>
        cleaned = re.sub(r'<pre class="code-block">.*?</pre>', '', cleaned, flags=re.DOTALL)
        
        raw_latex = re.findall(r'\\[a-zA-Z]+', cleaned)
        if raw_latex:
            print(f"[RAW LATEX] {fname}: {raw_latex}")
            
        # Check B2_17, B2_18, B2_19, B2_22, B3_4 visible content
        if fname in ["B2_17.html", "B2_18.html", "B2_19.html", "B2_22.html", "B3_4.html"]:
            print(f"=== {fname} ===")
            # print de-bai, answer, subtitle, guide
            for line in visible.splitlines():
                line_s = line.strip()
                if any(k in line_s for k in ["Đề bài", "Kiểm tra", "Kết quả", "Hình vẽ cho", "Hướng dẫn", "<li>"]):
                    print("  ", line_s[:120])

if __name__ == "__main__":
    check_everything()
