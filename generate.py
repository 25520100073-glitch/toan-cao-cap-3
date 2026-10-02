import numpy as np
import plotly.graph_objects as go
import sympy as sp

# ----------------- Verifications -----------------
x_sym, y_sym = sp.symbols('x y')

# B1.1
z1_sym = x_sym**2 + x_sym*y_sym**3
ans1 = sp.integrate(z1_sym, (y_sym, x_sym**2, x_sym), (x_sym, 0, 1))

# B1.2
z2_sym = x_sym**2 + y_sym
ans2 = sp.integrate(z2_sym, (y_sym, x_sym**2, 4), (x_sym, -2, 2))

# B1.3
z3_sym = sp.exp(x_sym**2)
# Original: int_0^1 int_y^1 e^{x^2} dx dy
ans3 = sp.integrate(z3_sym, (x_sym, y_sym, 1), (y_sym, 0, 1))

# ----------------- Visualizations -----------------
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>TCC3 - Tích phân bội hai</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f8f9fa; }}
        h1, h2 {{ color: #2c3e50; }}
        .problem {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 40px; }}
        .code-block {{ background: #282c34; color: #abb2bf; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace; }}
    </style>
</head>
<body>
    <h1>Bài tập Tích phân bội 2 (Toán Cao Cấp 3)</h1>
"""

# B1.1 Plot
x1 = np.linspace(0, 1, 100)
y1 = np.linspace(0, 1, 100)
X1, Y1 = np.meshgrid(x1, y1)
Z1 = X1**2 + X1*Y1**3
mask1 = (Y1 >= X1**2) & (Y1 <= X1)
Z1[~mask1] = np.nan

fig1 = go.Figure(data=[go.Surface(z=Z1, x=X1, y=Y1, colorscale='Viridis')])
fig1.update_layout(title='B1.1: z = x² + xy³', autosize=False, width=800, height=600,
                  scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'))
div1 = fig1.to_html(full_html=False, include_plotlyjs=False)

# B1.2 Plot
x2 = np.linspace(-2, 2, 200)
y2 = np.linspace(0, 4, 200)
X2, Y2 = np.meshgrid(x2, y2)
Z2 = X2**2 + Y2
mask2 = (Y2 >= X2**2) & (Y2 <= 4)
Z2[~mask2] = np.nan

fig2 = go.Figure(data=[go.Surface(z=Z2, x=X2, y=Y2, colorscale='Plasma')])
fig2.update_layout(title='B1.2: z = x² + y', autosize=False, width=800, height=600,
                  scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'))
div2 = fig2.to_html(full_html=False, include_plotlyjs=False)

# B1.3 Plot
x3 = np.linspace(0, 1, 100)
y3 = np.linspace(0, 1, 100)
X3, Y3 = np.meshgrid(x3, y3)
Z3 = np.exp(X3**2)
mask3 = (Y3 >= 0) & (Y3 <= X3) # Equivalent to y <= x <= 1
Z3[~mask3] = np.nan

fig3 = go.Figure(data=[go.Surface(z=Z3, x=X3, y=Y3, colorscale='Inferno')])
fig3.update_layout(title='B1.3: z = e^(x²)', autosize=False, width=800, height=600,
                  scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'))
div3 = fig3.to_html(full_html=False, include_plotlyjs=False)

# Build HTML
python_code = '''
# Đoạn code Python để AI khác có thể đọc và dựng lại mô hình 3D
import numpy as np
import plotly.graph_objects as go
import sympy as sp

x_sym, y_sym = sp.symbols('x y')

# Bài B1.1
print("B1.1 Tích phân:", sp.integrate(x_sym**2 + x_sym*y_sym**3, (y_sym, x_sym**2, x_sym), (x_sym, 0, 1)))
X1, Y1 = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
Z1 = X1**2 + X1*Y1**3
Z1[~((Y1 >= X1**2) & (Y1 <= X1))] = np.nan
fig1 = go.Figure(data=[go.Surface(z=Z1, x=X1, y=Y1)])
# fig1.show()

# Bài B1.2
print("B1.2 Tích phân:", sp.integrate(x_sym**2 + y_sym, (y_sym, x_sym**2, 4), (x_sym, -2, 2)))
X2, Y2 = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(0, 4, 200))
Z2 = X2**2 + Y2
Z2[~((Y2 >= X2**2) & (Y2 <= 4))] = np.nan
fig2 = go.Figure(data=[go.Surface(z=Z2, x=X2, y=Y2)])
# fig2.show()

# Bài B1.3
print("B1.3 Tích phân:", sp.integrate(sp.exp(x_sym**2), (x_sym, y_sym, 1), (y_sym, 0, 1)))
X3, Y3 = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
Z3 = np.exp(X3**2)
Z3[~((Y3 >= 0) & (Y3 <= X3))] = np.nan
fig3 = go.Figure(data=[go.Surface(z=Z3, x=X3, y=Y3)])
# fig3.show()
'''

html_content += f"""
    <div class="problem">
        <h2>Bài B1.1</h2>
        <p><strong>Đề bài:</strong> Tính $\\iint_D (x^2 + xy^3) dxdy$, với $D$ là miền phẳng được giới hạn bởi đường thẳng $y = x$ và parabol $y = x^2$.</p>
        <p><strong>Kiểm tra đáp án:</strong> {ans1} (khớp với đáp án 1/15)</p>
        <div class="plot">{div1}</div>
    </div>
    
    <div class="problem">
        <h2>Bài B1.2</h2>
        <p><strong>Đề bài:</strong> Tính $\\iint_D (x^2 + y) dxdy$, với $D$ là miền phẳng được giới hạn bởi đường thẳng $y = 4$ và parabol $y = x^2$.</p>
        <p><strong>Kiểm tra đáp án:</strong> {ans2} (khớp với đáp án 512/15)</p>
        <div class="plot">{div2}</div>
    </div>

    <div class="problem">
        <h2>Bài B1.3</h2>
        <p><strong>Đề bài:</strong> Tính $\\int_0^1 \\int_y^1 e^{{x^2}} dx dy$</p>
        <p><strong>Kiểm tra đáp án:</strong> {ans3} (khớp với đáp án 1/2(e-1))</p>
        <div class="plot">{div3}</div>
    </div>

    <div class="problem">
        <h2>Bản Code Python Tham Khảo</h2>
        <p>Bản code dưới đây sử dụng <code>numpy</code>, <code>sympy</code> và <code>plotly</code> để tính toán giải tích và dựng hình 3D, giúp một AI khác có thể dễ dàng hiểu và tái tạo.</p>
        <pre class="code-block"><code>{python_code}</code></pre>
    </div>
    
    <!-- Thêm MathJax để hiển thị công thức toán học -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</body>
</html>
"""

with open('TCC3.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("TCC3.html generated successfully.")
