import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f8f9fa; line-height: 1.8; }}
        h2 {{ color: #1a252f; border-bottom: 2px solid #2980b9; padding-bottom: 8px; }}
        h3 {{ color: #2980b9; margin-top: 24px; }}
        .problem {{ background: white; padding: 28px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.12); margin-bottom: 40px; max-width: 900px; margin-left: auto; margin-right: auto; }}
        .de-bai {{ background: #eaf4fb; border-left: 5px solid #2980b9; padding: 12px 18px; border-radius: 4px; margin-bottom: 16px; }}
        .solution {{ background: #f9f9f9; border-left: 5px solid #27ae60; padding: 14px 18px; border-radius: 4px; margin-bottom: 16px; }}
        .solution p, .solution li {{ margin: 6px 0; }}
        .solution ol {{ margin: 0; padding-left: 22px; }}
        .answer-box {{ background: #fff8e1; border: 2px solid #f39c12; padding: 10px 18px; border-radius: 4px; font-weight: bold; display: inline-block; margin-top: 8px; }}
        .check {{ background: #eafaf1; border-left: 4px solid #27ae60; padding: 8px 14px; border-radius: 4px; margin-top: 10px; color: #1e8449; }}
        .plot-container {{ display: flex; justify-content: center; margin-top: 20px; }}
        .code-block {{ background: #282c34; color: #abb2bf; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace; font-size: 13px; margin-top: 10px; white-space: pre; }}
    </style>
</head>
<body>
    <div class="problem">
        <h2>{title}</h2>
        <div class="de-bai"><strong>Đề bài:</strong> {statement}</div>
        <h3>&#9998; Lời giải</h3>
        <div class="solution">{solution_html}</div>
        <div class="answer-box">&#10003; Kết quả: {answer}</div>
        <div class="check">{check_html}</div>
        <h3>&#128202; Hình minh họa</h3>
        <div class="plot-container">{plot_div}</div>
        <h3>&#128187; Mã nguồn Python (tham khảo)</h3>
        <pre class="code-block">{code}</pre>
    </div>
</body>
</html>
"""

def add_math_axes(traces, x_max=3, y_max=3, z_max=3, x_min=0, y_min=0, z_min=0):
    # Add origin O
    traces.append(go.Scatter3d(x=[0], y=[0], z=[0], mode='text', text=['O'], textposition='bottom left', showlegend=False, textfont=dict(size=14)))
    
    # Draw X axis
    traces.append(go.Scatter3d(x=[x_min, x_max], y=[0, 0], z=[0, 0], mode='lines', line=dict(color='black', width=3), showlegend=False))
    traces.append(go.Cone(x=[x_max], y=[0], z=[0], u=[1], v=[0], w=[0], sizemode='absolute', sizeref=0.15, showscale=False, colorscale=[[0, 'black'], [1, 'black']]))
    traces.append(go.Scatter3d(x=[x_max+0.1], y=[0], z=[0], mode='text', text=['x'], textposition='middle right', showlegend=False, textfont=dict(size=16)))

    # Draw Y axis
    traces.append(go.Scatter3d(x=[0, 0], y=[y_min, y_max], z=[0, 0], mode='lines', line=dict(color='black', width=3), showlegend=False))
    traces.append(go.Cone(x=[0], y=[y_max], z=[0], u=[0], v=[1], w=[0], sizemode='absolute', sizeref=0.15, showscale=False, colorscale=[[0, 'black'], [1, 'black']]))
    traces.append(go.Scatter3d(x=[0], y=[y_max+0.1], z=[0], mode='text', text=['y'], textposition='top center', showlegend=False, textfont=dict(size=16)))

    # Draw Z axis
    traces.append(go.Scatter3d(x=[0, 0], y=[0, 0], z=[z_min, z_max], mode='lines', line=dict(color='black', width=3), showlegend=False))
    traces.append(go.Cone(x=[0], y=[0], z=[z_max], u=[0], v=[0], w=[1], sizemode='absolute', sizeref=0.15, showscale=False, colorscale=[[0, 'black'], [1, 'black']]))
    traces.append(go.Scatter3d(x=[0], y=[0], z=[z_max+0.1], mode='text', text=['z'], textposition='top center', showlegend=False, textfont=dict(size=16)))

def create_3d_projection_html(filename, title, statement, answer_str, surface_traces, line_traces, domain_traces, code_str, solution_html="", check_html="", axis_extent=2.5):
    fig = make_subplots(
        rows=2, cols=1,
        row_heights=[0.65, 0.35],
        vertical_spacing=0.05,
        specs=[[{"type": "surface"}],
               [{"type": "xy"}]],
        subplot_titles=("", "Hình chiếu D trên mặt phẳng Oxy")
    )

    # Inject math axes
    math_axes_traces = []
    e = axis_extent
    add_math_axes(math_axes_traces, x_max=e, y_max=e, z_max=e, x_min=-0.3, y_min=-0.3, z_min=-0.3)

    for t in surface_traces + line_traces + math_axes_traces:
        fig.add_trace(t, row=1, col=1)

    for t in domain_traces:
        fig.add_trace(t, row=2, col=1)

    # Hide all default 3D axes
    no_axis = dict(
        showbackground=False,
        showgrid=False,
        showline=False,
        zeroline=False,
        showticklabels=False,
        title=''
    )

    fig.update_layout(
        title=title,
        height=900,
        width=800,
        margin=dict(l=0, r=0, t=50, b=0),
        showlegend=False,
        scene=dict(
            xaxis=no_axis,
            yaxis=no_axis,
            zaxis=no_axis,
            camera=dict(
                up=dict(x=0, y=0, z=1),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=1.8, y=-1.5, z=0.8)
            ),
            aspectmode='data'
        )
    )

    fig.update_xaxes(title_text="x", zeroline=True, zerolinecolor="black", zerolinewidth=2, row=2, col=1)
    fig.update_yaxes(title_text="y", zeroline=True, zerolinecolor="black", zerolinewidth=2, scaleanchor="x", scaleratio=1, row=2, col=1)

    plot_div = fig.to_html(full_html=False, include_plotlyjs=True)

    filepath = os.path.join(r"C:\Users\khải\.gemini\antigravity\scratch\TCC3", filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(HTML_TEMPLATE.format(
            title=title,
            statement=statement,
            solution_html=solution_html,
            answer=answer_str,
            check_html=check_html,
            plot_div=plot_div,
            code=code_str
        ))
    print(f"Generated {filename}")
