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
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f8f9fa; }}
        h1, h2 {{ color: #2c3e50; }}
        .problem {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 40px; }}
        .code-block {{ background: #282c34; color: #abb2bf; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace; }}
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

# Common 2D layout
layout_2d = dict(
    xaxis=dict(title='Trục x', zeroline=True, zerolinecolor='black', zerolinewidth=2, showgrid=True, gridcolor='lightgray'),
    yaxis=dict(title='Trục y', zeroline=True, zerolinecolor='black', zerolinewidth=2, showgrid=True, gridcolor='lightgray'),
    plot_bgcolor='white',
    width=700,
    height=700,
    hovermode="x unified"
)

# ==============================
# B1.1
# ==============================
ans1 = sp.integrate(x_sym**2 + x_sym*y_sym**3, (y_sym, x_sym**2, x_sym), (x_sym, 0, 1))
x1 = np.linspace(-0.2, 1.2, 300)
y1_line = x1
y1_para = x1**2

fig1 = go.Figure()
# Add shaded region D (x from 0 to 1)
x1_fill = np.linspace(0, 1, 100)
fig1.add_trace(go.Scatter(x=x1_fill, y=x1_fill**2, mode='lines', line=dict(width=0), showlegend=False, hoverinfo='skip'))
fig1.add_trace(go.Scatter(x=x1_fill, y=x1_fill, mode='lines', fill='tonexty', fillcolor='rgba(0, 176, 246, 0.4)', line=dict(width=0), name='Miền D'))

# Add border lines
fig1.add_trace(go.Scatter(x=x1, y=y1_para, mode='lines', line=dict(color='blue', width=2), name='Parabol y = x²'))
fig1.add_trace(go.Scatter(x=x1, y=y1_line, mode='lines', line=dict(color='red', width=2), name='Đường thẳng y = x'))

fig1.update_layout(title='Miền D: Giới hạn bởi y = x và y = x²', **layout_2d)
fig1.update_yaxes(range=[-0.2, 1.2])
div1 = fig1.to_html(full_html=False, include_plotlyjs=True)

code1 = """import numpy as np
import plotly.graph_objects as go
import sympy as sp
x, y = sp.symbols('x y')
print(sp.integrate(x**2 + x*y**3, (y, x**2, x), (x, 0, 1)))

x_val = np.linspace(0, 1, 100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_val, y=x_val**2, mode='lines', line=dict(width=0), showlegend=False))
fig.add_trace(go.Scatter(x=x_val, y=x_val, mode='lines', fill='tonexty', name='Miền D'))
fig.show()"""

with open(os.path.join(output_dir, 'B1_1.html'), 'w', encoding='utf-8') as f:
    f.write(html_template.format(title="Bài B1.1", statement=r"Tính \(\iint_D (x^2 + xy^3) dxdy\), với \(D\) là miền phẳng được giới hạn bởi đường thẳng \(y = x\) và parabol \(y = x^2\).", answer=f"\({sp.latex(ans1)}\) (khớp với đáp án 1/15)", plot_div=div1, code=code1))

# ==============================
# B1.2
# ==============================
ans2 = sp.integrate(x_sym**2 + y_sym, (y_sym, x_sym**2, 4), (x_sym, -2, 2))
x2 = np.linspace(-2.5, 2.5, 300)
y2_para = x2**2
y2_line = np.full_like(x2, 4)

fig2 = go.Figure()
# Shaded region D
x2_fill = np.linspace(-2, 2, 100)
fig2.add_trace(go.Scatter(x=x2_fill, y=x2_fill**2, mode='lines', line=dict(width=0), showlegend=False, hoverinfo='skip'))
fig2.add_trace(go.Scatter(x=x2_fill, y=np.full_like(x2_fill, 4), mode='lines', fill='tonexty', fillcolor='rgba(255, 127, 14, 0.4)', line=dict(width=0), name='Miền D'))

fig2.add_trace(go.Scatter(x=x2, y=y2_para, mode='lines', line=dict(color='blue', width=2), name='Parabol y = x²'))
fig2.add_trace(go.Scatter(x=x2, y=y2_line, mode='lines', line=dict(color='red', width=2), name='Đường thẳng y = 4'))

fig2.update_layout(title='Miền D: Giới hạn bởi y = 4 và y = x²', **layout_2d)
fig2.update_yaxes(range=[-1, 5])
div2 = fig2.to_html(full_html=False, include_plotlyjs=True)

code2 = """import numpy as np
import plotly.graph_objects as go
import sympy as sp
x, y = sp.symbols('x y')
print(sp.integrate(x**2 + y, (y, x**2, 4), (x, -2, 2)))

x_val = np.linspace(-2, 2, 100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_val, y=x_val**2, mode='lines', line=dict(width=0), showlegend=False))
fig.add_trace(go.Scatter(x=x_val, y=np.full_like(x_val, 4), mode='lines', fill='tonexty', name='Miền D'))
fig.show()"""

with open(os.path.join(output_dir, 'B1_2.html'), 'w', encoding='utf-8') as f:
    f.write(html_template.format(title="Bài B1.2", statement=r"Tính \(\iint_D (x^2 + y) dxdy\), với \(D\) là miền phẳng được giới hạn bởi đường thẳng \(y = 4\) và parabol \(y = x^2\).", answer=f"\({sp.latex(ans2)}\) (khớp với đáp án 512/15)", plot_div=div2, code=code2))

# ==============================
# B1.3
# ==============================
ans3 = sp.integrate(sp.exp(x_sym**2), (x_sym, y_sym, 1), (y_sym, 0, 1))
x3 = np.linspace(-0.2, 1.2, 300)
y3_line_x = x3
y3_line_0 = np.zeros_like(x3)

fig3 = go.Figure()
x3_fill = np.linspace(0, 1, 100)
fig3.add_trace(go.Scatter(x=x3_fill, y=np.zeros_like(x3_fill), mode='lines', line=dict(width=0), showlegend=False, hoverinfo='skip'))
fig3.add_trace(go.Scatter(x=x3_fill, y=x3_fill, mode='lines', fill='tonexty', fillcolor='rgba(44, 160, 44, 0.4)', line=dict(width=0), name='Miền D'))
# We also have boundary x=1
fig3.add_trace(go.Scatter(x=[1, 1], y=[0, 1], mode='lines', line=dict(color='purple', width=2), name='Đường thẳng x = 1'))

fig3.add_trace(go.Scatter(x=x3, y=y3_line_x, mode='lines', line=dict(color='blue', width=2), name='Đường thẳng y = x'))
fig3.add_trace(go.Scatter(x=x3, y=y3_line_0, mode='lines', line=dict(color='red', width=2), name='Đường thẳng y = 0'))

fig3.update_layout(title='Miền D: Giới hạn bởi y = x, y = 0, x = 1', **layout_2d)
fig3.update_yaxes(range=[-0.2, 1.2])
div3 = fig3.to_html(full_html=False, include_plotlyjs=True)

code3 = """import numpy as np
import plotly.graph_objects as go
import sympy as sp
x, y = sp.symbols('x y')
print(sp.integrate(sp.exp(x**2), (x, y, 1), (y, 0, 1)))

x_val = np.linspace(0, 1, 100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_val, y=np.zeros_like(x_val), mode='lines', line=dict(width=0), showlegend=False))
fig.add_trace(go.Scatter(x=x_val, y=x_val, mode='lines', fill='tonexty', name='Miền D'))
fig.show()"""

with open(os.path.join(output_dir, 'B1_3.html'), 'w', encoding='utf-8') as f:
    f.write(html_template.format(title="Bài B1.3", statement=r"Tính \(\int_0^1 \int_y^1 e^{x^2} dx dy\)", answer=f"\({sp.latex(ans3)}\) (khớp với đáp án \(\\frac{{1}}{{2}}(e-1)\))", plot_div=div3, code=code3))

print("2D Separated HTML files generated successfully.")
