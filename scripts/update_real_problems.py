# -*- coding: utf-8 -*-
import os, re

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

b2_18 = r"""<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải - Bài B2.18</h3>
  <p><strong>Đề bài đầy đủ:</strong> Tính $I = \iint_D \sqrt{(4a^2-x^2-y^2)^3} dxdy$<br>với $D$ là miền nửa hình tròn tâm $A(a; 0)$, bán kính $a > 0$ nằm giữa $y=x$ và trục $Oy$ trong góc phần tư thứ nhất.</p>
  
  <p><strong>Bước 1: Phân tích miền D và chuyển sang tọa độ cực.</strong><br>
  Hình tròn tâm $A(a,0)$ bán kính $a$ có phương trình $(x-a)^2 + y^2 \le a^2 \iff x^2+y^2 \le 2ax$.<br>
  Trong tọa độ cực ($x = r\cos\theta, y = r\sin\theta$), phương trình này trở thành $r^2 \le 2ar\cos\theta \implies r \le 2a\cos\theta$.<br>
  Góc phần tư thứ nhất có $x \ge 0, y \ge 0$. Nằm giữa $y=x$ (tương ứng $\theta = \pi/4$) và trục $Oy$ (tương ứng $x=0 \implies \theta = \pi/2$).<br>
  Vậy miền $D$ trong tọa độ cực là:<br>
  $\pi/4 \le \theta \le \pi/2$<br>
  $0 \le r \le 2a\cos\theta$<br>
  Định thức Jacobi $J = r$.</p>
  
  <p><strong>Bước 2: Thiết lập tích phân.</strong><br>
  Hàm dưới dấu tích phân trở thành $\sqrt{(4a^2-r^2)^3} = (4a^2-r^2)^{3/2}$.<br>
  \[ I = \int_{\pi/4}^{\pi/2} d\theta \int_0^{2a\cos\theta} (4a^2-r^2)^{3/2} r \,dr \]
  </p>
  
  <p><strong>Bước 3: Tính tích phân theo r.</strong><br>
  Đặt $u = 4a^2-r^2 \implies du = -2r dr \implies r dr = -\frac{du}{2}$.<br>
  Đổi cận:<br>
  - Khi $r = 0 \implies u = 4a^2$.<br>
  - Khi $r = 2a\cos\theta \implies u = 4a^2 - 4a^2\cos^2\theta = 4a^2\sin^2\theta$.<br>
  Tích phân lớp trong:
  \[ I_r = \int_{4a^2}^{4a^2\sin^2\theta} u^{3/2} \left(-\frac{du}{2}\right) = \frac{1}{2} \int_{4a^2\sin^2\theta}^{4a^2} u^{3/2} \,du = \frac{1}{2} \left[ \frac{2}{5} u^{5/2} \right]_{4a^2\sin^2\theta}^{4a^2} \]
  \[ = \frac{1}{5} \left( (4a^2)^{5/2} - (4a^2\sin^2\theta)^{5/2} \right) = \frac{1}{5} \left( 32a^5 - 32a^5\sin^5\theta \right) = \frac{32a^5}{5} (1 - \sin^5\theta) \]
  </p>
  
  <p><strong>Bước 4: Tính tích phân theo $\theta$.</strong><br>
  \[ I = \frac{32a^5}{5} \int_{\pi/4}^{\pi/2} (1 - \sin^5\theta) d\theta \]
  Ta tách thành 2 tích phân. Phần thứ nhất: $\int_{\pi/4}^{\pi/2} 1 d\theta = \frac{\pi}{4}$.<br>
  Phần thứ hai: Tính $\int_{\pi/4}^{\pi/2} \sin^5\theta d\theta = \int_{\pi/4}^{\pi/2} (1-\cos^2\theta)^2 \sin\theta d\theta$.<br>
  Đặt $t = \cos\theta \implies dt = -\sin\theta d\theta$. Cận chạy từ $t = \frac{\sqrt{2}}{2}$ đến $t = 0$.<br>
  \[ \int_{\sqrt{2}/2}^0 (1-t^2)^2 (-dt) = \int_0^{\sqrt{2}/2} (t^4 - 2t^2 + 1) dt = \left[ \frac{t^5}{5} - \frac{2t^3}{3} + t \right]_0^{\sqrt{2}/2} \]
  Thay $t = \frac{\sqrt{2}}{2}$ vào, chú ý $(\frac{\sqrt{2}}{2})^3 = \frac{\sqrt{2}}{4}$ và $(\frac{\sqrt{2}}{2})^5 = \frac{\sqrt{2}}{8}$:<br>
  \[ = \frac{\sqrt{2}}{40} - \frac{2\sqrt{2}}{12} + \frac{\sqrt{2}}{2} = \sqrt{2} \left( \frac{3}{120} - \frac{20}{120} + \frac{60}{120} \right) = \frac{43\sqrt{2}}{120} \]
  Ghép lại ta được:
  \[ I = \frac{32a^5}{5} \left( \frac{\pi}{4} - \frac{43\sqrt{2}}{120} \right) = \frac{8\pi a^5}{5} - \frac{1376\sqrt{2} a^5}{600} = \frac{8\pi a^5}{5} - \frac{172\sqrt{2} a^5}{75} \]
  Quy đồng mẫu số 75:
  \[ I = \frac{120\pi a^5 - 172\sqrt{2} a^5}{75} = \frac{4a^5}{75}(30\pi - 43\sqrt{2}) \]
  </p>
  
  <p style="color:#1a5276; font-weight:bold;">\(\boxed{I = \frac{4a^5}{75}(30\pi - 43\sqrt{2})}\) ✓ Khớp hoàn toàn với đáp án!</p>
</div>"""

b2_19 = r"""<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải - Bài B2.19</h3>
  <p><strong>Đề bài đầy đủ:</strong> Tính $I = \iint_D x^2 y dxdy$<br>với $D$ là miền phẳng xác định bởi $2x \le x^2+y^2 \le 4x$ và $-x \le y \le x\sqrt{3}$.</p>
  
  <p><strong>Bước 1: Phân tích miền D và chuyển tọa độ cực.</strong><br>
  Đặt $x = r\cos\theta, y = r\sin\theta$, định thức Jacobi $J = r$.<br>
  Bất phương trình bán kính: $2x \le x^2+y^2 \le 4x \implies 2r\cos\theta \le r^2 \le 4r\cos\theta \implies 2\cos\theta \le r \le 4\cos\theta$.<br>
  Bất phương trình góc: $-x \le y \le x\sqrt{3} \implies -1 \le \frac{y}{x} \le \sqrt{3} \implies -1 \le \tan\theta \le \sqrt{3}$.<br>
  Vì $x \ge 0$ (do $x^2+y^2 \ge 2x \implies x \ge 0$ ở lân cận này), ta có góc $\theta \in [-\pi/4, \pi/3]$.</p>
  
  <p><strong>Bước 2: Thiết lập và tính tích phân.</strong><br>
  Hàm dưới dấu tích phân: $x^2y = (r\cos\theta)^2(r\sin\theta) = r^3\cos^2\theta\sin\theta$.<br>
  Nhân với Jacobi $r$, ta có:
  \[ I = \int_{-\pi/4}^{\pi/3} d\theta \int_{2\cos\theta}^{4\cos\theta} (r^3\cos^2\theta\sin\theta) r \,dr = \int_{-\pi/4}^{\pi/3} \cos^2\theta\sin\theta \,d\theta \int_{2\cos\theta}^{4\cos\theta} r^4 \,dr \]
  Tích phân lớp trong:
  \[ \int_{2\cos\theta}^{4\cos\theta} r^4 \,dr = \left[ \frac{r^5}{5} \right]_{2\cos\theta}^{4\cos\theta} = \frac{(4\cos\theta)^5 - (2\cos\theta)^5}{5} = \frac{1024 - 32}{5}\cos^5\theta = \frac{992}{5}\cos^5\theta \]
  </p>
  
  <p><strong>Bước 3: Tích phân theo góc $\theta$.</strong><br>
  Thay vào $I$:
  \[ I = \frac{992}{5} \int_{-\pi/4}^{\pi/3} \cos^7\theta \sin\theta \,d\theta \]
  Đặt $t = \cos\theta \implies dt = -\sin\theta d\theta$. Cận chạy từ $t = \cos(-\pi/4) = \frac{\sqrt{2}}{2}$ đến $t = \cos(\pi/3) = \frac{1}{2}$.<br>
  \[ I = \frac{992}{5} \int_{\sqrt{2}/2}^{1/2} t^7 (-dt) = \frac{992}{5} \int_{1/2}^{\sqrt{2}/2} t^7 dt = \frac{992}{5} \left[ \frac{t^8}{8} \right]_{1/2}^{\sqrt{2}/2} \]
  \[ = \frac{124}{5} \left( \left(\frac{\sqrt{2}}{2}\right)^8 - \left(\frac{1}{2}\right)^8 \right) = \frac{124}{5} \left( \frac{16}{256} - \frac{1}{256} \right) = \frac{124}{5} \times \frac{15}{256} \]
  Rút gọn: $\frac{124 \times 3}{256} = \frac{31 \times 3}{64} = \frac{93}{64}$.
  </p>
  
  <p style="color:#1a5276; font-weight:bold;">\(\boxed{I = \frac{93}{64}}\) ✓ Đáp án chính xác tuyệt đối!</p>
</div>"""

b2_22 = r"""<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải - Bài B2.22</h3>
  <p><strong>Đề bài đầy đủ:</strong> Tính tích phân $I = \iint_D xy dxdy$<br>với $D$ là hình bình hành với phương trình các cạnh là $x-y=0$, $x-y=1$, $2x+y=1$, $2x+y=3$.</p>
  
  <p><strong>Bước 1: Đổi biến số tổng quát.</strong><br>
  Nhìn vào phương trình 4 cạnh, ta lập tức đặt ẩn phụ:
  \[ u = x-y \]
  \[ v = 2x+y \]
  Khi đó miền $D$ biến thành miền chữ nhật $D'$ rất đơn giản: $0 \le u \le 1$ và $1 \le v \le 3$.<br>
  Ta cần biểu diễn $x, y$ theo $u, v$. Giải hệ phương trình:<br>
  Cộng 2 phương trình: $3x = u+v \implies x = \frac{u+v}{3}$.<br>
  Thay $x$ vào phương trình 1: $\frac{u+v}{3} - y = u \implies y = \frac{v-2u}{3}$.
  </p>
  
  <p><strong>Bước 2: Tính Jacobian.</strong><br>
  Tính định thức Jacobi ngược $J^{-1}$:
  \[ J^{-1} = \frac{\partial(u,v)}{\partial(x,y)} = \begin{vmatrix} 1 & -1 \\ 2 & 1 \end{vmatrix} = (1)(1) - (-1)(2) = 3 \]
  Do đó $|J| = \frac{1}{3} \implies dxdy = \frac{1}{3} dudv$.
  </p>
  
  <p><strong>Bước 3: Thay vào và tính tích phân.</strong><br>
  Hàm dưới dấu tích phân: $xy = \left(\frac{u+v}{3}\right)\left(\frac{v-2u}{3}\right) = \frac{v^2 - uv - 2u^2}{9}$.<br>
  \[ I = \iint_{D'} \frac{v^2 - uv - 2u^2}{9} \cdot \frac{1}{3} dudv = \frac{1}{27} \int_0^1 du \int_1^3 (v^2 - uv - 2u^2) dv \]
  Tính lớp trong theo $v$:
  \[ \int_1^3 (v^2 - uv - 2u^2) dv = \left[ \frac{v^3}{3} - u\frac{v^2}{2} - 2u^2 v \right]_1^3 \]
  \[ = \left( 9 - \frac{9u}{2} - 6u^2 \right) - \left( \frac{1}{3} - \frac{u}{2} - 2u^2 \right) = \frac{26}{3} - 4u - 4u^2 \]
  Tính lớp ngoài theo $u$:
  \[ I = \frac{1}{27} \int_0^1 \left( \frac{26}{3} - 4u - 4u^2 \right) du = \frac{1}{27} \left[ \frac{26}{3}u - 2u^2 - \frac{4}{3}u^3 \right]_0^1 \]
  \[ = \frac{1}{27} \left( \frac{26}{3} - 2 - \frac{4}{3} \right) = \frac{1}{27} \left( \frac{22}{3} - \frac{6}{3} \right) = \frac{1}{27} \times \frac{16}{3} = \frac{16}{81} \]
  </p>
  
  <p style="color:#1a5276; font-weight:bold;">\(\boxed{I = \frac{16}{81}}\) ✓ Kết quả hoàn toàn trùng khớp!</p>
</div>"""

b3_4 = r"""<div class="solution">
  <p><strong>Đề bài đầy đủ:</strong> Tính tích phân $\iiint_\Omega \sqrt{x^2+z^2} dxdydz$, trong đó $\Omega$ là vật thể giới hạn bởi mặt trụ $x^2+z^2=1$, mặt phẳng $y+z=2$ và mặt phẳng $Oxz$.</p>
  
  <p><strong>Bước 1: Xác định giới hạn miền $\Omega$.</strong><br>
  - Mặt phẳng $Oxz$ chính là mặt $y=0$.<br>
  - Vật thể bị kẹp giữa $y=0$ và mặt phẳng chéo $y=2-z$. Vậy $0 \le y \le 2-z$.<br>
  - Hình chiếu của $\Omega$ lên mặt phẳng $Oxz$ (mặt cắt gốc) là hình tròn $D_{xz}: x^2+z^2 \le 1$.
  </p>
  
  <p><strong>Bước 2: Thiết lập tích phân lặp.</strong><br>
  Lấy tích phân theo biến $y$ trước:
  \[ I = \iint_{D_{xz}} \left( \int_0^{2-z} \sqrt{x^2+z^2} dy \right) dxdz = \iint_{D_{xz}} \sqrt{x^2+z^2} (2-z) dxdz \]
  </p>
  
  <p><strong>Bước 3: Chuyển sang tọa độ cực trong mặt phẳng Oxz.</strong><br>
  Đặt $x = r\cos\theta, z = r\sin\theta$. Khi đó $dx dz = r dr d\theta$.<br>
  Miền $D_{xz}$ là hình tròn đơn vị nên: $0 \le r \le 1$ và $0 \le \theta \le 2\pi$.<br>
  Hàm dưới dấu tích phân trở thành: $\sqrt{r^2} (2 - r\sin\theta) = r(2 - r\sin\theta)$.<br>
  Thay vào ta có:
  \[ I = \int_0^{2\pi} d\theta \int_0^1 r(2 - r\sin\theta) r dr = \int_0^{2\pi} d\theta \int_0^1 (2r^2 - r^3\sin\theta) dr \]
  </p>
  
  <p><strong>Bước 4: Tính toán.</strong><br>
  Tích phân lớp trong theo $r$:
  \[ \int_0^1 (2r^2 - r^3\sin\theta) dr = \left[ \frac{2}{3}r^3 - \frac{\sin\theta}{4}r^4 \right]_0^1 = \frac{2}{3} - \frac{\sin\theta}{4} \]
  Tích phân lớp ngoài theo $\theta$:
  \[ I = \int_0^{2\pi} \left( \frac{2}{3} - \frac{\sin\theta}{4} \right) d\theta = \left[ \frac{2}{3}\theta + \frac{\cos\theta}{4} \right]_0^{2\pi} \]
  \[ = \left( \frac{4\pi}{3} + \frac{1}{4} \right) - \left( 0 + \frac{1}{4} \right) = \frac{4\pi}{3} \]
  </p>
  <p style="color:#27ae60; font-weight:bold;">\(\boxed{I = \frac{4\pi}{3}}\) ✓ Tuyệt vời, đáp án hoàn toàn chính xác!</p>
</div>"""

def update_file(filename, solution_html, statement_html):
    filepath = os.path.join(BASE_DIR, filename + '.html')
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace the red warning box or old solution
    if filename.startswith('B2'):
        # Fix the problem statement text at the top
        text = re.sub(r'<p><strong>Đề bài:</strong>.*?</p>', f'<p><strong>Đề bài:</strong> {statement_html}</p>', text)
        
        # We need to find the red warning box we just added, or the original solution box.
        pattern = r'<div style="background:#(fdedec|eaf4fb); border-left:5px solid #(e74c3c|2980b9); padding:20px; margin-top:30px; border-radius:6px;">.*?</div>\s*(?=</div>\s*</body>)'
        text = re.sub(pattern, lambda m: solution_html, text, flags=re.DOTALL)
        
    else:
        # B3 style
        text = re.sub(r'<div class="de-bai"><strong>Đề bài:</strong>.*?</div>', f'<div class="de-bai"><strong>Đề bài:</strong> {statement_html}</div>', text)
        pattern = r'<div class="solution">.*?</div>'
        text = re.sub(pattern, lambda m: solution_html, text, flags=re.DOTALL)
        
        # Also fix the red warning box if it has one
        warning_pattern = r'<div style="background:#fdedec; border-left:5px solid #e74c3c; padding:20px; margin-top:30px; border-radius:6px;">.*?</div>\s*(?=<div class="answer-box">)'
        text = re.sub(warning_pattern, lambda m: solution_html, text, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    st_18 = r"Tính \(\iint_D \sqrt{(4a^2-x^2-y^2)^3} dxdy\) với \(D\) là miền nửa hình tròn tâm \(A(a; 0)\), bán kính \(a > 0\) nằm giữa \(y=x\) và trục \(Oy\) trong góc phần tư thứ nhất."
    update_file("B2_18", b2_18, st_18)
    
    st_19 = r"Tính \(\iint_D x^2 y dxdy\) với \(D\) là miền phẳng xác định bởi \(2x \le x^2+y^2 \le 4x\) và \(-x \le y \le x\sqrt{3}\)."
    update_file("B2_19", b2_19, st_19)
    
    st_22 = r"Tính tích phân \(\iint_D xy dxdy\) với \(D\) là hình bình hành với phương trình các cạnh là \(x-y=0, x-y=1, 2x+y=1, 2x+y=3\)."
    update_file("B2_22", b2_22, st_22)
    
    st_4 = r"Tính tích phân \(\iiint_\Omega \sqrt{x^2+z^2} dxdydz\), trong đó \(\Omega\) là vật thể giới hạn bởi mặt trụ \(x^2+z^2=1\), mặt phẳng \(y+z=2\) và mặt phẳng \(Oxz\)."
    update_file("B3_4", b3_4, st_4)
    print("Files updated with real problem statements and solutions.")
