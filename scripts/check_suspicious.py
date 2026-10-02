# -*- coding: utf-8 -*-
import os, re, glob

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

def inspect_all_solutions():
    for prefix, nmax in [("B1", 20), ("B2", 22), ("B3", 15)]:
        for i in range(1, nmax + 1):
            fname = f"{prefix}_{i}.html"
            fpath = os.path.join(BASE_DIR, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                text = f.read()
                
            p_start = text.find('<div class="plot-container">')
            p_end = text.rfind('</script>')
            visible = text[:p_start] + (text[p_end+9:] if p_end != -1 else "")
            
            # Check for suspicious words in visible text
            for bad in ["Sympy", "sympy", "B(", "Gamma", "\\dots", "...", "giả sử", "Giả sử", "giả định", "Giả định", "khuyết"]:
                if bad in visible:
                    # ignore code-block
                    no_code = re.sub(r'<pre class="code-block">.*?</pre>', '', visible, flags=re.DOTALL)
                    if bad in no_code:
                        print(f"[SUSPICIOUS '{bad}'] {fname}")

if __name__ == "__main__":
    inspect_all_solutions()
