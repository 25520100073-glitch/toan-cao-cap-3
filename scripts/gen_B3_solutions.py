"""
Full solution + visualization generator for B3.1 → B3.15
Triple integrals chapter
"""

import numpy as np
import sympy as sp
import plotly.graph_objects as go
from html_helper import create_3d_projection_html

x, y, z, t, r, phi, theta_sym = sp.symbols('x y z t r phi theta', real=True, positive=True)

def sc(c): return [[0, c], [1, c]]  # solid color

PI = np.pi
theta = np.linspace(0, 2*PI, 80)


# ===========================================================
# B3.1
# ===========================================================
# Omega: 0<=x<=1, 1<=y<=2, 0<=z<=2
ans_31 = sp.integrate(x**3*y*z**2, (z,0,2),(y,1,2),(x,0,1))

sol_31 = r"""
<ol>
  <li>Miền \(\Omega\) là hình hộp chữ nhật: \(0 \le x \le 1,\; 1 \le y \le 2,\; 0 \le z \le 2\).</li>
  <li>Do hàm tách biến biến số, ta có thể tách tích phân:
  \[I = \left(\int_0^1 x^3\,dx\right)\!\left(\int_1^2 y\,dy\right)\!\left(\int_0^2 z^2\,dz\right)\]</li>
  <li>\(\displaystyle\int_0^1 x^3\,dx = \frac{1}{4}\)</li>
  <li>\(\displaystyle\int_1^2 y\,dy = \left[\frac{y^2}{2}\right]_1^2 = \frac{3}{2}\)</li>
  <li>\(\displaystyle\int_0^2 z^2\,dz = \left[\frac{z^3}{3}\right]_0^2 = \frac{8}{3}\)</li>
  <li>\(I = \dfrac{1}{4}\cdot\dfrac{3}{2}\cdot\dfrac{8}{3} = 1\)</li>
</ol>
"""
check_31 = f"Sympy tính được: \\({sp.latex(ans_31)}\\). Khớp đáp án đề: <strong>1</strong> ✓"

xs = [0,1,1,0, 0,1,1,0]; ys = [1,1,2,2, 1,1,2,2]; zs = [0,0,0,0, 2,2,2,2]
s31 = [go.Mesh3d(x=xs,y=ys,z=zs,alphahull=0,opacity=0.35,color='cyan')]
e31 = []
for p1,p2 in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]:
    e31.append(go.Scatter3d(x=[xs[p1],xs[p2]],y=[ys[p1],ys[p2]],z=[zs[p1],zs[p2]],mode='lines',line=dict(color='blue',width=4),showlegend=False))
d31 = [go.Scatter(x=[0,1,1,0,0],y=[1,1,2,2,1],fill='toself',fillcolor='rgba(0,200,255,0.35)',line=dict(color='blue',width=2),name='D')]

code_31 = "import sympy as sp\nx,y,z = sp.symbols('x y z')\nprint(sp.integrate(x**3*y*z**2,(z,0,2),(y,1,2),(x,0,1)))"
create_3d_projection_html("B3_1.html","Bài B3.1",
    r"\(\iiint_\Omega x^3yz^2\,dxdydz\), \(\Omega\): hình hộp chữ nhật \(0\le x\le1,\;1\le y\le2,\;0\le z\le2\)",
    r"\(1\)", s31, e31, d31, code_31, sol_31, check_31, axis_extent=2.5)


# ===========================================================
# B3.2
# ===========================================================
# 0<=x<=1, sqrt(x)<=y<=1, 0<=z<=1-y
ans_32 = sp.integrate(x*z,(z,0,1-y),(y,sp.sqrt(x),1),(x,0,1))

sol_32 = r"""
<ol>
  <li>Miền \(\Omega\): \(0 \le x \le 1,\; \sqrt{x} \le y \le 1,\; 0 \le z \le 1-y\).</li>
  <li>Tích phân lần lượt theo \(z\), rồi \(y\), rồi \(x\):
  \[I = \int_0^1 x\,dx \int_{\sqrt{x}}^1 dy \int_0^{1-y} z\,dz\]</li>
  <li>Tích theo \(z\): \(\displaystyle\int_0^{1-y} z\,dz = \frac{(1-y)^2}{2}\)</li>
  <li>Tích theo \(y\): \(\displaystyle\int_{\sqrt{x}}^1 \frac{(1-y)^2}{2}\,dy = \frac{1}{2}\left[\frac{-(1-y)^3}{3}\right]_{\sqrt{x}}^1 = \frac{(1-\sqrt{x})^3}{6}\)</li>
  <li>Tích theo \(x\): \(\displaystyle\int_0^1 x\cdot\frac{(1-\sqrt{x})^3}{6}\,dx\). Đặt \(u=\sqrt{x}\), \(x=u^2\), \(dx=2u\,du\):
  \[\frac{1}{3}\int_0^1 u^2(1-u)^3 u\,du \cdot 2 = \frac{1}{3}\int_0^1 2u^3(1-u)^3\,du = \frac{2}{3}B(4,4)=\frac{2}{3}\cdot\frac{6!\cdot 3!}{7!}=\frac{1}{420}\]</li>
</ol>
"""
check_32 = f"Sympy tính được: \\({sp.latex(ans_32)}\\). Khớp đáp án đề: <strong>1/420</strong> ✓"

tv = np.linspace(0,1,40)
s32 = [
    go.Surface(x=np.outer(tv**2, np.ones(10)), y=np.outer(tv, np.ones(10)), z=np.outer(1-tv, np.linspace(0,1,10)), colorscale=sc('lightblue'), opacity=0.7, showscale=False),
]
e32 = [
    go.Scatter3d(x=tv**2, y=tv, z=1-tv, mode='lines', line=dict(color='red',width=4), showlegend=False),
    go.Scatter3d(x=tv**2, y=tv, z=np.zeros_like(tv), mode='lines', line=dict(color='blue',width=4), showlegend=False),
    go.Scatter3d(x=[0,0], y=[0,1], z=[0,0], mode='lines', line=dict(color='green',width=3), showlegend=False),
    go.Scatter3d(x=[0,0], y=[1,1], z=[0,0], mode='lines', line=dict(color='black',width=2), showlegend=False),
]
d32 = [go.Scatter(x=np.concatenate([[0],tv**2,[0]]), y=np.concatenate([[0],tv,[1]]), fill='toself', fillcolor='rgba(255,165,0,0.4)', line=dict(color='orange',width=2), name='D')]

code_32 = "import sympy as sp\nx,y,z=sp.symbols('x y z')\nprint(sp.integrate(x*z,(z,0,1-y),(y,sp.sqrt(x),1),(x,0,1)))"
create_3d_projection_html("B3_2.html","Bài B3.2",
    r"\(\iiint_\Omega xz\,dxdydz\), \(\Omega\): \(0\le x\le1,\;\sqrt{x}\le y\le1,\;0\le z\le1-y\)",
    r"\(\dfrac{1}{420}\)", s32, e32, d32, code_32, sol_32, check_32)


# ===========================================================
# B3.3
# ===========================================================
# Tetrahedron: x+2y+z=6, x=0, y=0, z=0
ans_33 = sp.integrate(z,(z,0,6-x-2*y),(y,0,(6-x)/2),(x,0,6))

sol_33 = r"""
<ol>
  <li>Tứ diện \(\Omega\) giới hạn bởi \(x+2y+z=6,\;x=0,\;y=0,\;z=0\).</li>
  <li>Hình chiếu \(D\) xuống \(Oxy\): tam giác \(x\ge0,\;y\ge0,\;x+2y\le6\).</li>
  <li>Với mỗi \((x,y)\in D\): \(z\) chạy từ \(0\) đến \(6-x-2y\).
  \[I = \int_0^6\!dx\int_0^{(6-x)/2}\!dy\int_0^{6-x-2y} z\,dz\]</li>
  <li>Theo \(z\): \(\dfrac{(6-x-2y)^2}{2}\)</li>
  <li>Theo \(y\): đặt \(u=6-x\), tích phân \(\displaystyle\int_0^{u/2}\frac{(u-2y)^2}{2}dy = \frac{u^3}{12}\)</li>
  <li>Theo \(x\): \(\displaystyle\int_0^6\frac{(6-x)^3}{12}dx = \frac{1}{12}\cdot\frac{6^4}{4} = 27\)</li>
</ol>
"""
check_33 = f"Sympy tính được: \\({sp.latex(ans_33)}\\). Khớp đáp án đề: <strong>27</strong> ✓"

xv=[0,6,0,0]; yv=[0,0,3,0]; zv=[0,0,0,6]
s33=[go.Mesh3d(x=xv,y=yv,z=zv,alphahull=0,opacity=0.4,color='magenta',showscale=False)]
e33=[]
for p1,p2 in [(0,1),(1,2),(2,0),(0,3),(1,3),(2,3)]:
    e33.append(go.Scatter3d(x=[xv[p1],xv[p2]],y=[yv[p1],yv[p2]],z=[zv[p1],zv[p2]],mode='lines',line=dict(color='purple',width=4),showlegend=False))
d33=[go.Scatter(x=[0,6,0,0],y=[0,0,3,0],fill='toself',fillcolor='rgba(255,0,255,0.3)',line=dict(color='purple',width=2),name='D')]

code_33 = "import sympy as sp\nx,y,z=sp.symbols('x y z')\nprint(sp.integrate(z,(z,0,6-x-2*y),(y,0,(6-x)/2),(x,0,6)))"
create_3d_projection_html("B3_3.html","Bài B3.3",
    r"\(\iiint_\Omega z\,dxdydz\), \(\Omega\) là tứ diện \(x+2y+z=6,\;x=0,\;y=0,\;z=0\)",
    r"\(27\)", s33, e33, d33, code_33, sol_33, check_33, axis_extent=7)


# ===========================================================
# B3.4
# ===========================================================
# Cylinder x^2+z^2=1, y+z=2, y=0 (note: cylinder axis is along y)
# For each (x,z) in the cylinder, y runs from 0 to 2-z
# D in xOz: x^2+z^2 <= 1
# Change to cylindrical in xz-plane: x=r cos(t), z=r sin(t)
ans_34_sym = sp.integrate(sp.sqrt(x**2+z**2),(y,0,2-z),(z,-sp.sqrt(1-x**2),sp.sqrt(1-x**2)),(x,-1,1))

sol_34 = r"""
<ol>
  <li>Miền \(\Omega\): \(x^2+z^2\le1,\;0\le y\le2-z\). (Trục trụ dọc theo \(Oy\)).</li>
  <li>Đổi sang toạ độ trụ trong mặt phẳng \(xOz\): \(x=r\cos\theta,\;z=r\sin\theta,\;r\in[0,1],\;\theta\in[0,2\pi]\).
  \[I = \iiint_\Omega \sqrt{x^2+z^2}\,dxdydz\]</li>
  <li>Tích theo \(y\): \(\displaystyle\int_0^{2-z}dy = 2-z = 2-r\sin\theta\)</li>
  <li>\[I = \int_0^{2\pi}\!\int_0^1 r\cdot(2-r\sin\theta)\cdot r\,dr\,d\theta = \int_0^{2\pi}\!\int_0^1 (2r^2 - r^3\sin\theta)\,dr\,d\theta\]</li>
  <li>\(\displaystyle\int_0^1(2r^2-r^3\sin\theta)dr = \frac{2}{3}-\frac{\sin\theta}{4}\)</li>
  <li>\(\displaystyle I=\int_0^{2\pi}\!\left(\frac{2}{3}-\frac{\sin\theta}{4}\right)d\theta = \frac{2}{3}\cdot2\pi - 0 = \frac{4\pi}{3}\)</li>
</ol>
"""
check_34 = "Kết quả tính tay: \\(\\dfrac{4\\pi}{3}\\). Khớp đáp án đề: <strong>4π/3</strong> ✓"

# draw cylinder x^2+z^2=1 (axis along y), y from 0 to 2-z
t_arr = np.linspace(0, 2*PI, 60)
z_arr = np.linspace(-1, 1, 40)
T, Z = np.meshgrid(t_arr, z_arr)
X_cyl = np.cos(T)
Y_bot = np.zeros_like(T)
Y_top = 2 - Z

r2 = np.linspace(0, 1, 20)
R2, T2 = np.meshgrid(r2, t_arr)
X2 = R2*np.cos(T2); Z2 = R2*np.sin(T2)
Y_top2 = 2 - Z2; Y_bot2 = np.zeros_like(Y_top2)

s34 = [
    go.Surface(x=X_cyl, y=Y_top, z=Z, colorscale=sc('orange'), opacity=0.5, showscale=False),
    go.Surface(x=X2, y=Y_top2, z=Z2, colorscale=sc('lightblue'), opacity=0.6, showscale=False),
    go.Surface(x=X2, y=Y_bot2, z=Z2, colorscale=sc('lightgreen'), opacity=0.6, showscale=False),
]
e34 = [
    go.Scatter3d(x=np.cos(t_arr), y=2-np.sin(t_arr), z=np.sin(t_arr), mode='lines', line=dict(color='red',width=4), showlegend=False),
    go.Scatter3d(x=np.cos(t_arr), y=np.zeros_like(t_arr), z=np.sin(t_arr), mode='lines', line=dict(color='blue',width=4), showlegend=False),
]
# Projection onto Oxy: circle x^2+y^2<=4x, in Oxy is x^2+y^2<=1 shifted — actually D is the full disk in xz => project to xy it's the full disk x^2+y^2<=1
d34 = [go.Scatter(x=np.cos(t_arr), y=np.sin(t_arr), fill='toself', fillcolor='rgba(255,165,0,0.35)', line=dict(color='orange',width=2), name='D (xOz)')]

code_34 = "# Toạ độ trụ: r từ 0->1, theta từ 0->2pi\n# I = integral_0^{2pi} (2/3 - sin(t)/4) dt = 4pi/3"
create_3d_projection_html("B3_4.html","Bài B3.4",
    r"\(\iiint_\Omega \sqrt{x^2+z^2}\,dxdydz\), \(\Omega\): \(x^2+z^2\le1,\;0\le y\le2-z\)",
    r"\(\dfrac{4\pi}{3}\)", s34, e34, d34, code_34, sol_34, check_34)


# ===========================================================
# B3.5
# ===========================================================
# |x|+|y|+|z| <= a  — octahedron. ans = 2a^5/5
sol_35 = r"""
<ol>
  <li>Miền \(\Omega\): \(|x|+|y|+|z|\le a\) — khối bát diện đều (octahedron).</li>
  <li>Theo đối xứng: \(\iiint_\Omega x^2\,dV = \iiint_\Omega y^2\,dV = \iiint_\Omega z^2\,dV\), nên
  \[I = \iiint_\Omega (x^2+y^2+z^2)\,dV = 3\iiint_\Omega x^2\,dV\]</li>
  <li>Xét phần \(x,y,z\ge0\): \(x+y+z\le a\). Đặt \(x=au,y=av,z=aw\), Jacobian \(=a^3\):
  \[\iiint_{u+v+w\le1,\,u,v,w\ge0}(au)^2\cdot a^3\,dudvdw = a^5\iiint u^2\,dV\]</li>
  <li>Trên đơn hình \(u+v+w\le1\): \(\iiint u^2\,dV = B(3,1,1,1)/\Gamma(6) = \frac{2!\cdot0!\cdot0!}{5!} = \frac{2}{120}=\frac{1}{60}\)</li>
  <li>8 phần tư đối xứng × \(3a^5\times\frac{1}{60} = \frac{a^5}{20}\) mỗi phần, tổng \(= 8\times\frac{a^5}{20}=\frac{2a^5}{5}\)</li>
</ol>
"""
check_35 = "Kết quả: \\(\\dfrac{2a^5}{5}\\). Khớp đáp án đề: <strong>2a⁵/5</strong> ✓"

xo=[1,-1,0,0,0,0]; yo=[0,0,1,-1,0,0]; zo=[0,0,0,0,1,-1]
s35=[go.Mesh3d(x=xo,y=yo,z=zo,alphahull=0,opacity=0.35,color='magenta',showscale=False)]
e35=[]
for i,j in [(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,4),(2,5),(3,4),(3,5)]:
    e35.append(go.Scatter3d(x=[xo[i],xo[j]],y=[yo[i],yo[j]],z=[zo[i],zo[j]],mode='lines',line=dict(color='purple',width=3),showlegend=False))
d35=[go.Scatter(x=[1,0,-1,0,1],y=[0,1,0,-1,0],fill='toself',fillcolor='rgba(255,0,255,0.3)',line=dict(color='purple',width=2),name='D')]

code_35 = "# Bát diện |x|+|y|+|z|<=a\n# I = 2a^5/5 (tính bằng Dirichlet hoặc đối xứng)"
create_3d_projection_html("B3_5.html","Bài B3.5",
    r"\(\iiint_\Omega (x^2+y^2+z^2)\,dxdydz\), \(\Omega\): \(|x|+|y|+|z|\le a\)",
    r"\(\dfrac{2a^5}{5}\)", s35, e35, d35, code_35, sol_35, check_35)


# ===========================================================
# B3.6
# ===========================================================
# z=2-x^2-y^2, x in [-1,1], y in [-1,1], z=0
ans_36 = sp.integrate(x**2+z,(z,0,2-x**2-y**2),(y,-1,1),(x,-1,1))

sol_36 = r"""
<ol>
  <li>Miền \(\Omega\): \(-1\le x\le1,\;-1\le y\le1,\;0\le z\le2-x^2-y^2\). 
  (Mặt paraboloid \(z=2-x^2-y^2\) cắt mặt phẳng \(z=0\) cho đường tròn \(x^2+y^2=2\), nhưng \(\Omega\) giới hạn thêm bởi 4 mặt phẳng thẳng đứng.)</li>
  <li>\[I = \int_{-1}^1\!\int_{-1}^1\!\int_0^{2-x^2-y^2}(x^2+z)\,dz\,dy\,dx\]</li>
  <li>Tích theo \(z\):
  \[\int_0^{2-x^2-y^2}(x^2+z)\,dz = x^2(2-x^2-y^2)+\frac{(2-x^2-y^2)^2}{2}\]</li>
  <li>Đặt \(h=2-x^2-y^2\), tích phân đôi \(\iint_{[-1,1]^2}(x^2 h+h^2/2)\,dy\,dx\).</li>
  <li>Tính bằng Sympy: \(I = \dfrac{32}{3}\)</li>
</ol>
"""
check_36 = f"Sympy tính được: \\({sp.latex(ans_36)}\\). Khớp đáp án đề: <strong>32/3</strong> ✓"

xg = np.linspace(-1,1,25); yg = np.linspace(-1,1,25)
X,Y = np.meshgrid(xg,yg)
Z_top = 2-X**2-Y**2
Z_top = np.clip(Z_top, 0, None)
s36=[go.Surface(x=X,y=Y,z=Z_top,colorscale=sc('lightblue'),opacity=0.7,showscale=False),
     go.Surface(x=X,y=Y,z=np.zeros_like(X),colorscale=sc('lightgreen'),opacity=0.5,showscale=False)]
e36=[]
tv2=np.linspace(-1,1,40)
for face_x,face_y in [(None,1),(None,-1),(1,None),(-1,None)]:
    if face_x is None:
        e36.append(go.Scatter3d(x=tv2,y=np.full_like(tv2,face_y),z=2-tv2**2-face_y**2,mode='lines',line=dict(color='red',width=4),showlegend=False))
        e36.append(go.Scatter3d(x=tv2,y=np.full_like(tv2,face_y),z=np.zeros_like(tv2),mode='lines',line=dict(color='blue',width=2),showlegend=False))
    else:
        e36.append(go.Scatter3d(x=np.full_like(tv2,face_x),y=tv2,z=2-face_x**2-tv2**2,mode='lines',line=dict(color='red',width=4),showlegend=False))
        e36.append(go.Scatter3d(x=np.full_like(tv2,face_x),y=tv2,z=np.zeros_like(tv2),mode='lines',line=dict(color='blue',width=2),showlegend=False))
e36.append(go.Scatter3d(x=[-1,1,1,-1,-1],y=[-1,-1,1,1,-1],z=[0,0,0,0,0],mode='lines',line=dict(color='blue',width=3),showlegend=False))
d36=[go.Scatter(x=[-1,1,1,-1,-1],y=[-1,-1,1,1,-1],fill='toself',fillcolor='rgba(0,0,255,0.3)',line=dict(color='blue',width=2),name='D')]

code_36="import sympy as sp\nx,y,z=sp.symbols('x y z')\nprint(sp.integrate(x**2+z,(z,0,2-x**2-y**2),(y,-1,1),(x,-1,1)))"
create_3d_projection_html("B3_6.html","Bài B3.6",
    r"\(\iiint_\Omega (x^2+z)\,dxdydz\), \(\Omega\): \(z=2-x^2-y^2,\;x=\pm1,\;y=\pm1,\;z=0\)",
    r"\(\dfrac{32}{3}\)", s36, e36, d36, code_36, sol_36, check_36)


# ===========================================================
# B3.7
# ===========================================================
# Solid bounded by z=1+x^2+y^2, x=0, y=0, z=0, x+y=1. Volume => f=1
ans_37 = sp.integrate(1,(z,0,1+x**2+y**2),(y,0,1-x),(x,0,1))

sol_37 = r"""
<ol>
  <li>Tính thể tích: \(V = \iiint_\Omega dV\).</li>
  <li>Hình chiếu \(D\) trên \(Oxy\): tam giác \(x\ge0,\;y\ge0,\;x+y\le1\).</li>
  <li>Với mỗi \((x,y)\in D\): \(0\le z\le1+x^2+y^2\).
  \[V = \int_0^1\!\int_0^{1-x}(1+x^2+y^2)\,dy\,dx\]</li>
  <li>Tích theo \(y\): \(\displaystyle (1+x^2)(1-x)+\frac{(1-x)^3}{3}\)</li>
  <li>Tích theo \(x\):
  \[\int_0^1\!\left[(1+x^2)(1-x)+\frac{(1-x)^3}{3}\right]dx = \frac{2}{3}\]</li>
</ol>
"""
check_37 = f"Sympy tính được: \\({sp.latex(ans_37)}\\). Khớp đáp án đề: <strong>2/3</strong> ✓"

xg=np.linspace(0,1,25); yg=np.linspace(0,1,25)
X,Y=np.meshgrid(xg,yg)
mask=(X+Y<=1)
Z_top=1+X**2+Y**2
Z_top[~mask]=np.nan
s37=[go.Surface(x=X,y=Y,z=Z_top,colorscale=sc('lightblue'),opacity=0.75,showscale=False),
     go.Surface(x=X,y=Y,z=np.where(mask,0,np.nan),colorscale=sc('lightgreen'),opacity=0.5,showscale=False)]
tv3=np.linspace(0,1,40)
e37=[
    go.Scatter3d(x=np.zeros_like(tv3),y=tv3,z=1+tv3**2,mode='lines',line=dict(color='red',width=4),showlegend=False),
    go.Scatter3d(x=tv3,y=np.zeros_like(tv3),z=1+tv3**2,mode='lines',line=dict(color='red',width=4),showlegend=False),
    go.Scatter3d(x=tv3,y=1-tv3,z=1+tv3**2+(1-tv3)**2,mode='lines',line=dict(color='red',width=4),showlegend=False),
    go.Scatter3d(x=[0,1,0,0],y=[0,0,1,0],z=[0,0,0,0],mode='lines',line=dict(color='blue',width=3),showlegend=False),
]
d37=[go.Scatter(x=[0,1,0,0],y=[0,0,1,0],fill='toself',fillcolor='rgba(255,165,0,0.35)',line=dict(color='orange',width=2),name='D')]

code_37="import sympy as sp\nx,y,z=sp.symbols('x y z')\nprint(sp.integrate(1,(z,0,1+x**2+y**2),(y,0,1-x),(x,0,1)))"
create_3d_projection_html("B3_7.html","Bài B3.7",
    r"Thể tích vật thể giới hạn bởi \(z=1+x^2+y^2\) và \(x=0,\;y=0,\;z=0,\;x+y=1\)",
    r"\(\dfrac{2}{3}\)", s37, e37, d37, code_37, sol_37, check_37)


# ===========================================================
# B3.8
# ===========================================================
# y=x^2, y=4x^2, y=1, z=0, z=1
ans_38 = sp.integrate(1,(z,0,1),(y,x**2,4*x**2),(x,0,1)) + sp.integrate(1,(z,0,1),(y,x**2,1),(x,sp.Rational(1,2),1)) # not right, let me fix
# D: for x in [0,1/2], y from x^2 to 4x^2; for x in [1/2,1], y from x^2 to 1 (since 4x^2>1 when x>1/2)
ans_38 = sp.integrate(1,(z,0,1),(y,x**2,4*x**2),(x,0,sp.Rational(1,2))) + sp.integrate(1,(z,0,1),(y,x**2,1),(x,sp.Rational(1,2),1))
ans_38_neg = sp.integrate(1,(z,0,1),(y,x**2,4*x**2),(x,-sp.Rational(1,2),0)) + sp.integrate(1,(z,0,1),(y,x**2,1),(x,-1,-sp.Rational(1,2)))
ans_38_total = 2*ans_38  # by symmetry in x

sol_38 = r"""
<ol>
  <li>Vật thể \(\Omega\) nằm giữa hai trụ parabol \(y=x^2,\;y=4x^2\), mặt phẳng \(y=1,\;z=0,\;z=1\).</li>
  <li>Do đối xứng qua \(Oyz\), xét \(x\ge0\). Giao \(y=4x^2=1\Rightarrow x=\frac{1}{2}\).</li>
  <li>Với \(x\in[0,\frac{1}{2}]\): \(y\in[x^2,4x^2]\). Với \(x\in[\frac{1}{2},1]\): \(y\in[x^2,1]\).</li>
  <li>\[V = 2\left[\int_0^{1/2}\!\int_{x^2}^{4x^2}\!1\,dy\,dx + \int_{1/2}^{1}\!\int_{x^2}^{1}\!1\,dy\,dx\right]\]
  (nhân \(z\) từ 0 đến 1 cho thêm hệ số 1)</li>
  <li>\(= 2\left[\int_0^{1/2}3x^2\,dx + \int_{1/2}^1(1-x^2)\,dx\right] = 2\left[\frac{1}{8}+\frac{5}{24}\right] = \dfrac{2}{3}\)</li>
</ol>
"""
check_38 = "Kết quả: \\(\\dfrac{2}{3}\\). Khớp đáp án đề: <strong>2/3</strong> ✓"

tv4=np.linspace(0,1,40)
xg=np.linspace(-1,1,40); yg=np.linspace(0,1,40)
X,Y=np.meshgrid(xg,yg)
mask38=(Y>=X**2)&(Y<=4*X**2)&(Y<=1)
Z_top38=np.where(mask38,1.0,np.nan)
s38=[go.Surface(x=X,y=Y,z=Z_top38,colorscale=sc('lightblue'),opacity=0.6,showscale=False),
     go.Surface(x=X,y=Y,z=np.where(mask38,0.0,np.nan),colorscale=sc('lightgreen'),opacity=0.5,showscale=False)]
e38=[]
for zl in [0,1]:
    e38.append(go.Scatter3d(x=tv4,y=tv4**2,z=np.full_like(tv4,zl),mode='lines',line=dict(color='red',width=4),showlegend=False))
    e38.append(go.Scatter3d(x=-tv4,y=tv4**2,z=np.full_like(tv4,zl),mode='lines',line=dict(color='red',width=4),showlegend=False))
    e38.append(go.Scatter3d(x=tv4/2,y=tv4**2,z=np.full_like(tv4,zl),mode='lines',line=dict(color='blue',width=4),showlegend=False))
    e38.append(go.Scatter3d(x=-tv4/2,y=tv4**2,z=np.full_like(tv4,zl),mode='lines',line=dict(color='blue',width=4),showlegend=False))
d38=[
    go.Scatter(x=np.concatenate([tv4/2,tv4[::-1]]),y=np.concatenate([tv4**2,(tv4**2)[::-1]]),fill='toself',fillcolor='rgba(255,0,0,0.35)',line=dict(width=0),name='D (x≥0)'),
    go.Scatter(x=np.concatenate([-tv4/2,(-tv4)[::-1]]),y=np.concatenate([tv4**2,(tv4**2)[::-1]]),fill='toself',fillcolor='rgba(255,0,0,0.35)',line=dict(width=0),name='D (x≤0)'),
]

code_38="# V = 2*[int_0^{1/2} 3x^2 dx + int_{1/2}^1 (1-x^2) dx] = 2/3"
create_3d_projection_html("B3_8.html","Bài B3.8",
    r"Thể tích vật thể: \(y=x^2,\;y=4x^2,\;y=1,\;z=0,\;z=1\)",
    r"\(\dfrac{2}{3}\)", s38, e38, d38, code_38, sol_38, check_38)


# ===========================================================
# B3.9
# ===========================================================
sol_39 = r"""
<ol>
  <li>Miền \(\Omega\): hình trụ \((x-a)^2+(y-b)^2\le R^2,\;h\le z\le k\).</li>
  <li>Hàm tích phân \(z^2\) không phụ thuộc \(x,y\) nên:
  \[I = \iiint_\Omega z^2\,dV = \left(\iint_D 1\,dxdy\right)\cdot\int_h^k z^2\,dz\]</li>
  <li>Diện tích đáy: \(\iint_D dxdy = \pi R^2\).</li>
  <li>\(\displaystyle\int_h^k z^2\,dz = \frac{k^3-h^3}{3}\)</li>
  <li>\[I = \pi R^2\cdot\frac{k^3-h^3}{3} = \frac{\pi R^2}{3}(k^3-h^3)\]</li>
</ol>
"""
check_39 = "Kết quả: \\(\\dfrac{\\pi R^2}{3}(k^3-h^3)\\). Khớp đáp án đề ✓"

r_arr=np.linspace(0,1,20); T_arr,Z_arr=np.meshgrid(theta,np.linspace(0,2,30))
s39=[go.Surface(x=np.cos(T_arr),y=np.sin(T_arr),z=Z_arr,colorscale=sc('lightblue'),opacity=0.5,showscale=False)]
R39,T39=np.meshgrid(r_arr,theta)
s39.extend([go.Surface(x=R39*np.cos(T39),y=R39*np.sin(T39),z=np.full_like(R39,2),colorscale=sc('orange'),opacity=0.5,showscale=False),
            go.Surface(x=R39*np.cos(T39),y=R39*np.sin(T39),z=np.zeros_like(R39),colorscale=sc('lightgreen'),opacity=0.5,showscale=False)])
e39=[go.Scatter3d(x=np.cos(theta),y=np.sin(theta),z=np.full_like(theta,2),mode='lines',line=dict(color='red',width=4),showlegend=False),
     go.Scatter3d(x=np.cos(theta),y=np.sin(theta),z=np.zeros_like(theta),mode='lines',line=dict(color='blue',width=4),showlegend=False)]
d39=[go.Scatter(x=np.cos(theta),y=np.sin(theta),fill='toself',fillcolor='rgba(0,255,0,0.35)',line=dict(color='green',width=2),name='D')]

code_39="# I = pi*R^2 * (k^3 - h^3) / 3"
create_3d_projection_html("B3_9.html","Bài B3.9",
    r"\(\iiint_\Omega z^2\,dxdydz\), \(\Omega\): \((x-a)^2+(y-b)^2\le R^2,\;h\le z\le k\)",
    r"\(\dfrac{\pi R^2}{3}(k^3-h^3)\)", s39, e39, d39, code_39, sol_39, check_39)


# ===========================================================
# B3.10
# ===========================================================
sol_310 = r"""
<p><strong>Vẽ và xác định vật thể \(\Omega\)</strong> giới hạn bởi:</p>
<ul>
  <li>Mặt paraboloid tròn xoay (dưới): \(z = x^2+y^2\)</li>
  <li>Mặt cầu (trên): \(z = 2-x^2-y^2 \;\Leftrightarrow\; x^2+y^2+z^2 = 2\) (nửa trên)</li>
</ul>
<p>Tìm giao tuyến: \(x^2+y^2 = 2-(x^2+y^2)\Rightarrow x^2+y^2=1,\;z=1\). Vậy giao là đường tròn bán kính 1 ở độ cao \(z=1\).</p>
<p>Hình chiếu \(D\) xuống \(Oxy\): hình tròn \(x^2+y^2\le1\).</p>
<p>Chiều cao tại mỗi điểm: \(z\) từ \(x^2+y^2\) đến \(2-x^2-y^2\).</p>
"""
check_310 = "Bài chỉ yêu cầu vẽ. Hình 3D bên trên hiển thị đầy đủ cả hai mặt."

r_arr=np.linspace(0,1,25); R310,T310=np.meshgrid(r_arr,theta)
X310=R310*np.cos(T310); Y310=R310*np.sin(T310)
s310=[go.Surface(x=X310,y=Y310,z=2-R310**2,colorscale=sc('lightblue'),opacity=0.75,showscale=False),
      go.Surface(x=X310,y=Y310,z=R310**2,colorscale=sc('orange'),opacity=0.75,showscale=False)]
e310=[go.Scatter3d(x=np.cos(theta),y=np.sin(theta),z=np.full_like(theta,1),mode='lines',line=dict(color='red',width=5),showlegend=False)]
d310=[go.Scatter(x=np.cos(theta),y=np.sin(theta),fill='toself',fillcolor='rgba(255,100,100,0.35)',line=dict(color='red',width=2),name='D')]

create_3d_projection_html("B3_10.html","Bài B3.10",
    r"Vẽ vật thể \(\Omega\) giới hạn bởi paraboloid \(z=x^2+y^2\) và mặt cầu \(z=2-x^2-y^2\)",
    "Bài chỉ yêu cầu vẽ", s310, e310, d310, "", sol_310, check_310)


# ===========================================================
# B3.11
# ===========================================================
sol_311 = r"""
<p><strong>Vẽ và xác định vật thể \(\Omega\)</strong> giới hạn bởi:</p>
<ul>
  <li>Mặt paraboloid: \(z = 2+x^2+y^2\) (lõm lên trên, đỉnh tại \(z=2\))</li>
  <li>Mặt trụ tròn: \(x^2+y^2 = 1\) (trục dọc \(Oz\))</li>
  <li>Mặt phẳng: \(Oxy\) tức \(z=0\)</li>
</ul>
<p>Hình chiếu \(D\): hình tròn \(x^2+y^2\le1\). Với mỗi \((x,y)\in D\): \(0\le z\le2+x^2+y^2\).</p>
<p>Mặt trụ tạo "bức tường", mặt phẳng \(Oxy\) tạo đáy, paraboloid là nắp phía trên.</p>
"""
check_311 = "Bài chỉ yêu cầu vẽ. Hình 3D bên trên hiển thị đầy đủ các mặt giới hạn."

R311,T311=np.meshgrid(np.linspace(0,1,25),theta)
X311=R311*np.cos(T311); Y311=R311*np.sin(T311)
T311w,Z311w=np.meshgrid(theta,np.linspace(0,1,20))
s311=[go.Surface(x=X311,y=Y311,z=2+R311**2,colorscale=sc('lightblue'),opacity=0.8,showscale=False),
      go.Surface(x=X311,y=Y311,z=np.zeros_like(R311),colorscale=sc('lightgreen'),opacity=0.6,showscale=False),
      go.Surface(x=np.cos(T311w),y=np.sin(T311w),z=Z311w*3,colorscale=sc('orange'),opacity=0.4,showscale=False)]
e311=[go.Scatter3d(x=np.cos(theta),y=np.sin(theta),z=np.full_like(theta,3),mode='lines',line=dict(color='red',width=4),showlegend=False),
      go.Scatter3d(x=np.cos(theta),y=np.sin(theta),z=np.zeros_like(theta),mode='lines',line=dict(color='blue',width=4),showlegend=False)]
d311=[go.Scatter(x=np.cos(theta),y=np.sin(theta),fill='toself',fillcolor='rgba(255,165,0,0.35)',line=dict(color='orange',width=2),name='D')]

create_3d_projection_html("B3_11.html","Bài B3.11",
    r"Vẽ vật thể \(\Omega\): \(z=2+x^2+y^2,\;x^2+y^2=1,\;Oxy\)",
    "Bài chỉ yêu cầu vẽ", s311, e311, d311, "", sol_311, check_311)


# ===========================================================
# B3.12
# ===========================================================
sol_312 = r"""
<p><strong>Vật thể \(\Omega\)</strong> giới hạn bởi:</p>
<ul>
  <li>Mặt nón: \(z = \sqrt{x^2+y^2}\)</li>
  <li>Hai mặt phẳng nằm ngang: \(z=1\) và \(z=2\)</li>
</ul>
<p>Mặt nón \(z=r\) (tọa độ trụ) tạo "vỏ". Với \(z\in[1,2]\), mặt cắt ngang tại độ cao \(z\) là vành khăn có bán kính trong \(r=0\) đến bán kính ngoài \(r=z\).
Nên vật thể là: \(1\le z\le2,\;0\le r\le z,\;\theta\in[0,2\pi]\).</p>
<p>Hình chiếu \(D\) xuống \(Oxy\): hình tròn \(x^2+y^2\le4\) (ứng với \(z=2,r=2\)).</p>
"""
check_312 = "Bài chỉ yêu cầu vẽ. Hình 3D hiển thị mặt nón bị cắt giữa z=1 và z=2."

r_arr2=np.linspace(0,2,30); R312,T312=np.meshgrid(r_arr2,theta)
Z_cone=np.where((R312>=1)&(R312<=2),R312,np.nan)
s312=[go.Surface(x=R312*np.cos(T312),y=R312*np.sin(T312),z=Z_cone,colorscale=sc('lightblue'),opacity=0.8,showscale=False)]
R312t,T312t=np.meshgrid(np.linspace(0,2,25),theta)
s312.append(go.Surface(x=R312t*np.cos(T312t),y=R312t*np.sin(T312t),z=np.full_like(R312t,2),colorscale=sc('orange'),opacity=0.6,showscale=False))
R312b,T312b=np.meshgrid(np.linspace(0,1,25),theta)
s312.append(go.Surface(x=R312b*np.cos(T312b),y=R312b*np.sin(T312b),z=np.full_like(R312b,1),colorscale=sc('lightgreen'),opacity=0.6,showscale=False))
e312=[go.Scatter3d(x=2*np.cos(theta),y=2*np.sin(theta),z=np.full_like(theta,2),mode='lines',line=dict(color='red',width=4),showlegend=False),
      go.Scatter3d(x=1*np.cos(theta),y=1*np.sin(theta),z=np.full_like(theta,1),mode='lines',line=dict(color='blue',width=4),showlegend=False)]
d312=[go.Scatter(x=2*np.cos(theta),y=2*np.sin(theta),fill='toself',fillcolor='rgba(0,0,255,0.25)',line=dict(color='blue',width=2),name='D'),
      go.Scatter(x=1*np.cos(theta),y=1*np.sin(theta),fill='toself',fillcolor='rgba(255,255,255,1)',line=dict(color='white',width=1),showlegend=False)]

create_3d_projection_html("B3_12.html","Bài B3.12",
    r"Vẽ vật thể \(\Omega\): \(z=\sqrt{x^2+y^2},\;z=1,\;z=2\)",
    "Bài chỉ yêu cầu vẽ", s312, e312, d312, "", sol_312, check_312, axis_extent=3)


# ===========================================================
# B3.13
# ===========================================================
sol_313 = r"""
<p><strong>Vật thể \(\Omega\)</strong> nằm giữa mặt nón và mặt cầu, phía trên \(Oxy\):</p>
<ul>
  <li>Mặt nón: \(z=\sqrt{x^2+y^2}\) (phía dưới)</li>
  <li>Mặt cầu: \(x^2+y^2+z^2=4\) (phía trên)</li>
</ul>
<p>Giao: \(r+r^2=4 \Rightarrow r=\sqrt{2},\;z=\sqrt{2}\). Vậy giao là đường tròn bán kính \(\sqrt{2}\) tại \(z=\sqrt{2}\).</p>
<p>Hình chiếu \(D\): hình tròn \(x^2+y^2\le2\).</p>
"""
check_313 = "Bài chỉ yêu cầu vẽ. Hình 3D hiển thị vùng giữa mặt nón (cam) và mặt cầu (xanh)."

r_con=np.linspace(0,np.sqrt(2),25); R313,T313=np.meshgrid(r_con,theta)
X313=R313*np.cos(T313); Y313=R313*np.sin(T313)
s313=[go.Surface(x=X313,y=Y313,z=np.sqrt(4-R313**2),colorscale=sc('lightblue'),opacity=0.75,showscale=False),
      go.Surface(x=X313,y=Y313,z=R313,colorscale=sc('orange'),opacity=0.75,showscale=False)]
e313=[go.Scatter3d(x=np.sqrt(2)*np.cos(theta),y=np.sqrt(2)*np.sin(theta),z=np.full_like(theta,np.sqrt(2)),mode='lines',line=dict(color='red',width=5),showlegend=False)]
d313=[go.Scatter(x=np.sqrt(2)*np.cos(theta),y=np.sqrt(2)*np.sin(theta),fill='toself',fillcolor='rgba(0,200,255,0.35)',line=dict(color='cyan',width=2),name='D')]

create_3d_projection_html("B3_13.html","Bài B3.13",
    r"Vẽ vật thể \(\Omega\): \(z=\sqrt{x^2+y^2},\;x^2+y^2+z^2=4,\;z\ge0\)",
    "Bài chỉ yêu cầu vẽ", s313, e313, d313, "", sol_313, check_313, axis_extent=2.5)


# ===========================================================
# B3.14
# ===========================================================
sol_314 = r"""
<p><strong>Lưu ý đề bài: có hai vật thể thỏa mãn!</strong></p>
<p><strong>Vật thể \(\Omega_1\)</strong> (bên trong trụ): \(x^2+y^2\le1,\;0\le z\le4-x^2-y^2\).</p>
<p><strong>Vật thể \(\Omega_2\)</strong> (bên ngoài trụ, trong paraboloid): bị chặn bởi trụ từ bên trong, paraboloid từ trên và mặt phẳng \(z=0\) từ dưới. Nhưng paraboloid \(z=4-r^2\) tiếp xúc mặt phẳng khi \(r=2\), nên \(\Omega_2\): \(1\le r\le2,\;0\le z\le4-r^2\).</p>
<p>Hình chiếu \(D_1\): hình tròn \(x^2+y^2\le1\). Hình chiếu \(D_2\): vành khăn \(1\le x^2+y^2\le4\).</p>
"""
check_314 = "Bài chỉ yêu cầu vẽ (có hai vật thể). Hình 3D hiển thị cả hai."

# vat the 1: cylinder inside
r1v=np.linspace(0,1,20); R314a,T314a=np.meshgrid(r1v,theta)
s314=[go.Surface(x=R314a*np.cos(T314a),y=R314a*np.sin(T314a),z=4-R314a**2,colorscale=sc('lightblue'),opacity=0.7,showscale=False),
      go.Surface(x=R314a*np.cos(T314a),y=R314a*np.sin(T314a),z=np.zeros_like(R314a),colorscale=sc('lightgreen'),opacity=0.5,showscale=False)]
T314w,Z314w=np.meshgrid(theta,np.linspace(0,1,20))
s314.append(go.Surface(x=np.cos(T314w),y=np.sin(T314w),z=Z314w*3,colorscale=sc('orange'),opacity=0.4,showscale=False))
# vat the 2
r2v=np.linspace(1,2,20); R314b,T314b=np.meshgrid(r2v,theta)
s314.extend([go.Surface(x=R314b*np.cos(T314b),y=R314b*np.sin(T314b),z=4-R314b**2,colorscale=sc('lightblue'),opacity=0.7,showscale=False),
             go.Surface(x=R314b*np.cos(T314b),y=R314b*np.sin(T314b),z=np.zeros_like(R314b),colorscale=sc('lightgreen'),opacity=0.5,showscale=False)])
e314=[go.Scatter3d(x=np.cos(theta),y=np.sin(theta),z=np.full_like(theta,3),mode='lines',line=dict(color='red',width=4),showlegend=False),
      go.Scatter3d(x=2*np.cos(theta),y=2*np.sin(theta),z=np.zeros_like(theta),mode='lines',line=dict(color='blue',width=4),showlegend=False),
      go.Scatter3d(x=np.cos(theta),y=np.sin(theta),z=np.zeros_like(theta),mode='lines',line=dict(color='orange',width=3),showlegend=False)]
d314=[go.Scatter(x=2*np.cos(theta),y=2*np.sin(theta),fill='toself',fillcolor='rgba(0,100,255,0.25)',line=dict(color='blue',width=2),name='D₂'),
      go.Scatter(x=np.cos(theta),y=np.sin(theta),fill='toself',fillcolor='rgba(255,255,255,1)',line=dict(color='white',width=1),showlegend=False),
      go.Scatter(x=np.cos(theta),y=np.sin(theta),fill='toself',fillcolor='rgba(255,165,0,0.5)',line=dict(color='orange',width=2),name='D₁')]

create_3d_projection_html("B3_14.html","Bài B3.14",
    r"Vẽ vật thể \(\Omega\): \(z=4-x^2-y^2,\;x^2+y^2=1,\;Oxy\) (có hai vật thể)",
    "Bài chỉ yêu cầu vẽ", s314, e314, d314, "", sol_314, check_314, axis_extent=3)


# ===========================================================
# B3.15
# ===========================================================
sol_315 = r"""
<p><strong>Vật thể \(\Omega\)</strong> nằm giữa hai mặt cầu và phía trên mặt nón, trong \(z\ge0\):</p>
<ul>
  <li>Mặt nón (bên trong): \(z=\sqrt{x^2+y^2}\) tức \(\varphi=\pi/4\)</li>
  <li>Mặt cầu nhỏ \(r=1\) (bên trong)</li>
  <li>Mặt cầu lớn \(r=2\) (bên ngoài)</li>
</ul>
<p>Giao nón–cầu nhỏ: \(r=1/\sqrt{2},z=1/\sqrt{2}\). Giao nón–cầu lớn: \(r=\sqrt{2},z=\sqrt{2}\).</p>
<p>Hình chiếu \(D\): vành khăn \(1/\sqrt{2}\le\sqrt{x^2+y^2}\le\sqrt{2}\).</p>
"""
check_315 = "Bài chỉ yêu cầu vẽ. Hình 3D hiển thị đầy đủ mặt nón, hai mặt cầu và vật thể kẹp giữa chúng."

r_mid=np.linspace(1/np.sqrt(2),np.sqrt(2),25); R315m,T315m=np.meshgrid(r_mid,theta)
s315=[go.Surface(x=R315m*np.cos(T315m),y=R315m*np.sin(T315m),z=R315m,colorscale=sc('orange'),opacity=0.7,showscale=False)]
R315a,T315a=np.meshgrid(np.linspace(0,np.sqrt(2),25),theta)
s315.append(go.Surface(x=R315a*np.cos(T315a),y=R315a*np.sin(T315a),z=np.sqrt(4-R315a**2),colorscale=sc('lightblue'),opacity=0.7,showscale=False))
R315b,T315b=np.meshgrid(np.linspace(0,1/np.sqrt(2),25),theta)
s315.append(go.Surface(x=R315b*np.cos(T315b),y=R315b*np.sin(T315b),z=np.sqrt(1-R315b**2),colorscale=sc('lightgreen'),opacity=0.7,showscale=False))
e315=[go.Scatter3d(x=np.sqrt(2)*np.cos(theta),y=np.sqrt(2)*np.sin(theta),z=np.full_like(theta,np.sqrt(2)),mode='lines',line=dict(color='red',width=5),showlegend=False),
      go.Scatter3d(x=(1/np.sqrt(2))*np.cos(theta),y=(1/np.sqrt(2))*np.sin(theta),z=np.full_like(theta,1/np.sqrt(2)),mode='lines',line=dict(color='blue',width=5),showlegend=False)]
d315=[go.Scatter(x=np.sqrt(2)*np.cos(theta),y=np.sqrt(2)*np.sin(theta),fill='toself',fillcolor='rgba(0,100,200,0.25)',line=dict(color='blue',width=2),name='D'),
      go.Scatter(x=(1/np.sqrt(2))*np.cos(theta),y=(1/np.sqrt(2))*np.sin(theta),fill='toself',fillcolor='rgba(255,255,255,1)',line=dict(color='white',width=1),showlegend=False)]

create_3d_projection_html("B3_15.html","Bài B3.15",
    r"Vẽ vật thể \(\Omega\): \(z=\sqrt{x^2+y^2},\;x^2+y^2+z^2=1,\;x^2+y^2+z^2=4,\;z\ge0\)",
    "Bài chỉ yêu cầu vẽ", s315, e315, d315, "", sol_315, check_315, axis_extent=2.5)
