import numpy as np
import plotly.graph_objects as go
import sympy as sp
import os

output_dir = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"
os.makedirs(output_dir, exist_ok=True)
x_sym, y_sym = sp.symbols('x y')

html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f8f9fa; line-height: 1.6; }}
        h1, h2 {{ color: #2c3e50; }}
        .problem {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 40px; }}
        .code-block {{ background: #282c34; color: #abb2bf; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace; font-size: 14px; }}
        .plot-container {{ display: flex; justify-content: center; }}
    </style>
</head>
<body>
    <div class="problem">
        <h2>{title}</h2>
        <p><strong>Đề bài:</strong> {statement}</p>
        <p><strong>Kiểm tra đáp án:</strong> {answer}</p>
        <div class="plot-container">{plot_div}</div>
        
        <h3>Mã Nguồn Tham Khảo (Cho AI khác)</h3>
        <pre class="code-block"><code>{code}</code></pre>
    </div>
</body>
</html>
"""

layout_2d = dict(
    xaxis=dict(title='x', zeroline=True, zerolinecolor='black', zerolinewidth=2, showgrid=True, gridcolor='lightgray'),
    yaxis=dict(title='y', zeroline=True, zerolinecolor='black', zerolinewidth=2, showgrid=True, gridcolor='lightgray'),
    plot_bgcolor='white',
    width=700,
    height=700,
    hovermode="x unified"
)

# ==============================
# B1.4
# ==============================
ans4 = sp.integrate(x_sym**3 * y_sym, (y_sym, 0, sp.sqrt(1 - x_sym**2)), (x_sym, 0, 1))
x4 = np.linspace(0, 1, 300)
y4_curve = np.sqrt(1 - x4**2)

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=x4, y=np.zeros_like(x4), mode='lines', line=dict(width=0), showlegend=False, hoverinfo='skip'))
fig4.add_trace(go.Scatter(x=x4, y=y4_curve, mode='lines', fill='tonexty', fillcolor='rgba(0, 176, 246, 0.4)', line=dict(width=0), name='Miền D'))
fig4.add_trace(go.Scatter(x=x4, y=y4_curve, mode='lines', line=dict(color='blue', width=2), name='Đường tròn x² + y² = 1'))
fig4.add_trace(go.Scatter(x=[0, 0], y=[0, 1], mode='lines', line=dict(color='red', width=2), name='Trục Oy (x = 0)'))
fig4.add_trace(go.Scatter(x=[0, 1], y=[0, 0], mode='lines', line=dict(color='green', width=2), name='Trục Ox (y = 0)'))
fig4.update_layout(title='Miền D: Hình tròn đơn vị góc phần tư thứ nhất', **layout_2d)
# Force aspect ratio to be equal so circle looks like a circle
fig4.update_yaxes(scaleanchor="x", scaleratio=1, range=[-0.2, 1.2])
fig4.update_xaxes(range=[-0.2, 1.2])
div4 = fig4.to_html(full_html=False, include_plotlyjs=True)

code4 = """import numpy as np
import plotly.graph_objects as go
import sympy as sp
x, y = sp.symbols('x y')
ans = sp.integrate(x**3 * y, (y, 0, sp.sqrt(1 - x**2)), (x, 0, 1))
print(ans)

x_val = np.linspace(0, 1, 300)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_val, y=np.zeros_like(x_val), mode='lines', line=dict(width=0), showlegend=False))
fig.add_trace(go.Scatter(x=x_val, y=np.sqrt(1 - x_val**2), mode='lines', fill='tonexty', name='Miền D'))
fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.show()"""

with open(os.path.join(output_dir, 'B1_4.html'), 'w', encoding='utf-8') as f:
    f.write(html_template.format(title="Bài B1.4", statement=r"Tính \(\iint_D x^3y dxdy\), với \(D\) là phần hình tròn đơn vị \(x^2 + y^2 \le 1\) lấy trong miền \(x \ge 0\) và \(y \ge 0\).", answer=f"\({sp.latex(ans4)}\) (khớp với đáp án 1/24)", plot_div=div4, code=code4))

# ==============================
# B1.5
# ==============================
# Đổi thứ tự tính tích phân, no numerical answer for integral since f(x,y) is abstract.
# The domain is bounded by y = sqrt(x) and y = sqrt(2-x^2), 0 <= x <= 1
x5 = np.linspace(0, 1.5, 300)
# full circle arc x^2 + y^2 = 2 for context
x5_circ = np.linspace(0, np.sqrt(2), 300)
y5_circ = np.sqrt(2 - x5_circ**2)
y5_para = np.sqrt(x5)

fig5 = go.Figure()
x5_fill = np.linspace(0, 1, 100)
y5_fill_bottom = np.sqrt(x5_fill)
y5_fill_top = np.sqrt(2 - x5_fill**2)
fig5.add_trace(go.Scatter(x=x5_fill, y=y5_fill_bottom, mode='lines', line=dict(width=0), showlegend=False, hoverinfo='skip'))
fig5.add_trace(go.Scatter(x=x5_fill, y=y5_fill_top, mode='lines', fill='tonexty', fillcolor='rgba(255, 127, 14, 0.4)', line=dict(width=0), name='Miền D'))

fig5.add_trace(go.Scatter(x=x5_circ, y=y5_circ, mode='lines', line=dict(color='blue', width=2), name='Đường tròn y = √(2 - x²)'))
fig5.add_trace(go.Scatter(x=x5, y=y5_para, mode='lines', line=dict(color='red', width=2), name='Parabol y = √x'))
fig5.add_trace(go.Scatter(x=[0, 0], y=[0, 1.5], mode='lines', line=dict(color='purple', width=2, dash='dash'), name='Trục Oy (x=0)'))

fig5.update_layout(title='Miền D: Giữa y = √x và y = √(2 - x²)', **layout_2d)
fig5.update_yaxes(scaleanchor="x", scaleratio=1, range=[-0.2, 1.6])
fig5.update_xaxes(range=[-0.2, 1.6])
div5 = fig5.to_html(full_html=False, include_plotlyjs=True)

code5 = """import numpy as np
import plotly.graph_objects as go

x_val = np.linspace(0, 1, 100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_val, y=np.sqrt(x_val), mode='lines', line=dict(width=0), showlegend=False))
fig.add_trace(go.Scatter(x=x_val, y=np.sqrt(2 - x_val**2), mode='lines', fill='tonexty', name='Miền D'))
fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.show()"""

with open(os.path.join(output_dir, 'B1_5.html'), 'w', encoding='utf-8') as f:
    f.write(html_template.format(title="Bài B1.5", statement=r"Đổi thứ tự tính tích phân: \(\int_0^1 dx \int_{\sqrt{x}}^{\sqrt{2-x^2}} f(x;y) dy\).", answer="Không yêu cầu tính giá trị (bài toán đổi thứ tự).", plot_div=div5, code=code5))

# ==============================
# B1.6
# ==============================
ans6 = sp.integrate(y_sym, (y_sym, x_sym**2, 4 - x_sym**2 + 2*x_sym), (x_sym, -1, 2))
x6 = np.linspace(-1.5, 2.5, 300)
y6_p1 = x6**2
y6_p2 = 4 - x6**2 + 2*x6

fig6 = go.Figure()
x6_fill = np.linspace(-1, 2, 100)
fig6.add_trace(go.Scatter(x=x6_fill, y=x6_fill**2, mode='lines', line=dict(width=0), showlegend=False, hoverinfo='skip'))
fig6.add_trace(go.Scatter(x=x6_fill, y=4 - x6_fill**2 + 2*x6_fill, mode='lines', fill='tonexty', fillcolor='rgba(44, 160, 44, 0.4)', line=dict(width=0), name='Miền D'))

fig6.add_trace(go.Scatter(x=x6, y=y6_p1, mode='lines', line=dict(color='blue', width=2), name='Parabol y = x²'))
fig6.add_trace(go.Scatter(x=x6, y=y6_p2, mode='lines', line=dict(color='red', width=2), name='Parabol y = 4 - x² + 2x'))

fig6.update_layout(title='Miền D: Giới hạn bởi 2 parabol', **layout_2d)
fig6.update_yaxes(range=[-1, 6])
div6 = fig6.to_html(full_html=False, include_plotlyjs=True)

code6 = """import numpy as np
import plotly.graph_objects as go
import sympy as sp
x, y = sp.symbols('x y')
ans = sp.integrate(y, (y, x**2, 4 - x**2 + 2*x), (x, -1, 2))
print(ans)

x_val = np.linspace(-1, 2, 100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_val, y=x_val**2, mode='lines', line=dict(width=0), showlegend=False))
fig.add_trace(go.Scatter(x=x_val, y=4 - x_val**2 + 2*x_val, mode='lines', fill='tonexty', name='Miền D'))
fig.show()"""

with open(os.path.join(output_dir, 'B1_6.html'), 'w', encoding='utf-8') as f:
    f.write(html_template.format(title="Bài B1.6", statement=r"Tính \(\iint_D y dxdy\), với \(D\) là miền phẳng giới hạn bởi parabol \(y = x^2\) và parabol \(y = 4 - x^2 + 2x\).", answer=f"\({sp.latex(ans6)}\) (khớp với đáp án 45/2)", plot_div=div6, code=code6))

# ==============================
# B1.7
# ==============================
ans7 = sp.integrate(x_sym**2 * y_sym, (y_sym, 0, 3 - x_sym**2), (x_sym, -sp.sqrt(3), sp.sqrt(3)))
x7 = np.linspace(-2, 2, 300)
y7_p = 3 - x7**2

fig7 = go.Figure()
x7_fill = np.linspace(-np.sqrt(3), np.sqrt(3), 100)
fig7.add_trace(go.Scatter(x=x7_fill, y=np.zeros_like(x7_fill), mode='lines', line=dict(width=0), showlegend=False, hoverinfo='skip'))
fig7.add_trace(go.Scatter(x=x7_fill, y=3 - x7_fill**2, mode='lines', fill='tonexty', fillcolor='rgba(148, 103, 189, 0.4)', line=dict(width=0), name='Miền D'))

fig7.add_trace(go.Scatter(x=x7, y=y7_p, mode='lines', line=dict(color='blue', width=2), name='Parabola y = 3 - x²'))
fig7.add_trace(go.Scatter(x=x7, y=np.zeros_like(x7), mode='lines', line=dict(color='red', width=2), name='Trục Ox (y = 0)'))

fig7.update_layout(title='Miền D: Giới hạn bởi y = 3 - x² và trục Ox', **layout_2d)
fig7.update_yaxes(range=[-1, 4])
div7 = fig7.to_html(full_html=False, include_plotlyjs=True)

code7 = """import numpy as np
import plotly.graph_objects as go
import sympy as sp
x, y = sp.symbols('x y')
ans = sp.integrate(x**2 * y, (y, 0, 3 - x**2), (x, -sp.sqrt(3), sp.sqrt(3)))
print(ans)

x_val = np.linspace(-np.sqrt(3), np.sqrt(3), 100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_val, y=np.zeros_like(x_val), mode='lines', line=dict(width=0), showlegend=False))
fig.add_trace(go.Scatter(x=x_val, y=3 - x_val**2, mode='lines', fill='tonexty', name='Miền D'))
fig.show()"""

with open(os.path.join(output_dir, 'B1_7.html'), 'w', encoding='utf-8') as f:
    f.write(html_template.format(title="Bài B1.7", statement=r"Tính \(\iint_D x^2y dxdy\), với \(D\) là miền phẳng giới hạn bởi parabola \(y = 3 - x^2\) và trục \(Ox\).", answer=f"\({sp.latex(ans7)}\) (khớp với đáp án \(72\sqrt{{3}}/35\))", plot_div=div7, code=code7))

print("2D Separated HTML files (B1.4 - B1.7) generated successfully.")
