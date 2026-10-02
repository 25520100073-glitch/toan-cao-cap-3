# -*- coding: utf-8 -*-
import os, re

filepath = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3\B2_17.html"

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the original short problem statement
new_statement = r"Tính \(\iint_D \frac{\ln(\sqrt{x^2+y^2}+2)}{(\sqrt{x^2+y^2}+2)\sqrt{x^2+y^2}} dxdy\) với \(D: (e-2)^2 \le x^2+y^2 \le (e^2-2)^2\)"
text = re.sub(r'\\iint_D \\frac{\\ln\(\\sqrt\{x\^2\+y\^2\}\+2\)}{\\dots} dxdy', new_statement, text)

# Write the detailed solution
solution_html = r"""<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải - Bài B2.17</h3>
  <p><strong>Đề bài đầy đủ:</strong> Tính \(I = \iint_D \frac{\ln(\sqrt{x^2+y^2}+2)}{(\sqrt{x^2+y^2}+2)\sqrt{x^2+y^2}} dxdy\)<br>
  với miền \(D: (e-2)^2 \le x^2+y^2 \le (e^2-2)^2\).</p>
  
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  Đặt \(x = r\cos\theta\), \(y = r\sin\theta\). Ta có \(\sqrt{x^2+y^2} = r\).<br>
  Định thức Jacobi \(J = r\).<br>
  Từ bất phương trình biên của \(D\), bán kính \(r\) thỏa mãn: \((e-2)^2 \le r^2 \le (e^2-2)^2\)<br>
  Lấy căn bậc hai (vì \(r \ge 0\) và \(e \approx 2.718 > 2\)):<br>
  \(e-2 \le r \le e^2-2\).<br>
  Góc \(\theta\) quét trọn một vòng: \(0 \le \theta \le 2\pi\).</p>
  
  <p><strong>Bước 2: Thay vào tích phân lặp.</strong><br>
  Hàm dưới dấu tích phân trở thành: \(\frac{\ln(r+2)}{(r+2)r}\).<br>
  Khi nhân với định thức Jacobi \(r\), ta được biểu thức đơn giản hơn:
  \[I = \int_0^{2\pi} d\theta \int_{e-2}^{e^2-2} \frac{\ln(r+2)}{(r+2)r} \cdot r \,dr = \int_0^{2\pi} d\theta \int_{e-2}^{e^2-2} \frac{\ln(r+2)}{r+2} \,dr\]
  Tích phân theo \(\theta\) đơn giản bằng \(2\pi\):
  \[I = 2\pi \int_{e-2}^{e^2-2} \frac{\ln(r+2)}{r+2} \,dr\]</p>
  
  <p><strong>Bước 3: Tính tích phân bằng phương pháp đổi biến.</strong><br>
  Xét tích phân \(I_r = \int_{e-2}^{e^2-2} \frac{\ln(r+2)}{r+2} \,dr\).<br>
  Đặt \(u = \ln(r+2) \Rightarrow du = \frac{1}{r+2} dr\).<br>
  Đổi cận:<br>
  - Khi \(r = e-2 \Rightarrow u = \ln(e-2+2) = \ln(e) = 1\).<br>
  - Khi \(r = e^2-2 \Rightarrow u = \ln(e^2-2+2) = \ln(e^2) = 2\).<br>
  Thay vào \(I_r\):
  \[I_r = \int_1^2 u \,du = \left[ \frac{u^2}{2} \right]_1^2 = \frac{2^2}{2} - \frac{1^2}{2} = 2 - \frac{1}{2} = \frac{3}{2}\]
  Nhân lại với phần góc:
  \[I = 2\pi \cdot \frac{3}{2} = 3\pi\]</p>
  
  <p style="color:#1a5276; font-weight:bold;">\(\boxed{I = 3\pi}\) ✓ Cảm ơn bạn đã cung cấp đề bài hoàn chỉnh!</p>
</div>"""

pattern = r'<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">.*?</div>\s*(?=</div>\s*</body>)'
new_text = re.sub(pattern, lambda m: solution_html, text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated B2_17 successfully")
