# -*- coding: utf-8 -*-
import os, re

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

missing_texts = {
    "B2_18": "Đề bài đang bị khuyết phần giới hạn miền D. Đang chờ bạn cung cấp đề gốc (hình ảnh) để giải chính xác, không tự suy diễn.",
    "B2_19": "Đề bài cho miền D giới hạn bởi $2x \le x^2+y^2 \le 4x$, tích phân toàn miền sẽ bằng 0 do đối xứng. Chắc chắn đề bị khuyết một điều kiện (ví dụ $y \ge 0$). Đang chờ bạn xác nhận đề gốc.",
    "B2_22": "Đề bài chỉ ghi 'D là hình bình hành' nhưng khuyết thông tin về tọa độ đỉnh hoặc phương trình cạnh. Đang chờ đề gốc.",
    "B3_4": "Đề bài ghi $\iiint_\Omega \dots$ (khuyết mất hàm dưới dấu tích phân). Đang chờ bạn cung cấp hàm số gốc để giải tiếp."
}

def clear_fake_solutions():
    for fname, msg in missing_texts.items():
        path = os.path.join(BASE_DIR, fname + ".html")
        if not os.path.exists(path): continue
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        replacement = f"""<div style="background:#fdedec; border-left:5px solid #e74c3c; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#c0392b;">⚠️ Cảnh báo: Khuyết thiếu đề bài</h3>
  <p><strong>Báo cáo:</strong> {msg}</p>
</div>"""
        
        # Replace the solution div (either B2 style or B3 style)
        if fname.startswith("B2"):
            pattern = r'<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">.*?</div>\s*(?=</div>\s*</body>)'
        else:
            pattern = r'<div class="solution">.*?</div>'
            
        content = re.sub(pattern, lambda m: replacement, content, flags=re.DOTALL)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    clear_fake_solutions()
    print("Cleared fake solutions.")
