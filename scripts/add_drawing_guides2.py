# -*- coding: utf-8 -*-
import os, re

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

def generate_drawing_guide(eq_text):
    eq_clean = eq_text.replace(' ', '').replace('\\', '').replace('{', '').replace('}', '')
    is_3d = 'iiint' in eq_clean or 'z=' in eq_clean or 'z\\le' in eq_clean or 'z<' in eq_clean or 'dxdydz' in eq_clean or 'Vậtthể' in eq_clean or 'vậtthể' in eq_clean or 'z' in eq_text
    
    if ('iint' in eq_clean and 'iiint' not in eq_clean) and ('dxdydz' not in eq_clean) and ('z' not in eq_clean):
        is_3d = False
    if 'dxdy' in eq_clean and 'dz' not in eq_clean:
        is_3d = False

    guide_html = """
<div style="background:#fff3cd; border-left:5px solid #ffc107; padding:15px; margin:20px 0; border-radius:6px; font-size:14px; color:#555;">
  <h4 style="color:#b9770e; margin-top:0; margin-bottom:10px;">&#127912; Hướng dẫn chi tiết cách vẽ hình</h4>
  <ul style="margin:0; padding-left:20px; line-height:1.6;">
"""
    
    items = []
    
    if is_3d:
        if 'x^2+y^2+z^2' in eq_clean:
            items.append("<strong>Mặt cầu (dạng x² + y² + z² = R²):</strong> Chấm gốc tọa độ O. Vẽ một đường tròn xích đạo nằm ngang, rồi vẽ thêm các đường elip dọc để tạo hiệu ứng khối cầu 3D căng phồng.")
        if 'z=x^2+y^2' in eq_clean or 'z=2x^2+2y^2' in eq_clean:
            items.append("<strong>Mặt Paraboloid (dạng z = x² + y²):</strong> Có dạng như 'chiếc chảo'. Xác định đỉnh tại gốc O, uốn bề lõm hướng lên trên ôm lấy trục Oz. Mặt cắt ngang luôn là các đường tròn.")
        if 'z=2-x^2-y^2' in eq_clean or 'z=4-x^2-y^2' in eq_clean or '-x^2-y^2' in eq_clean:
            items.append("<strong>Mặt Paraboloid úp (dạng z = a - x² - y²):</strong> Giống 'chiếc bát úp ngược'. Đỉnh nằm ở điểm (0,0,a) trên trục Oz, uốn bề lõm chúc xuống dưới mặt sàn Oxy.")
        if 'z=sqrt(x^2+y^2)' in eq_clean or ('z' in eq_clean and 'sqrt(x^2+y^2)' in eq_clean):
            items.append("<strong>Mặt Nón (dạng z = √(x² + y²)):</strong> Đỉnh nằm tại gốc O. Vẽ hai đường thẳng (đường sinh) xòe ra tạo thành hình phễu, tạo góc nhọn 45 độ với trục đứng Oz.")
        if 'x^2+y^2=' in eq_clean and ('z' not in eq_clean.split('x^2+y^2=')[1][:4]):
            items.append("<strong>Mặt Trụ đứng (dạng x² + y² = R²):</strong> Vẽ một đường tròn dưới mặt đất (Oxy), rồi từ viền đường tròn kéo các đường sinh thẳng đứng song song với trục Oz thành hình ống.")
        if 'x^2+z^2=' in eq_clean:
            items.append("<strong>Mặt Trụ ngang (dạng x² + z² = R²):</strong> Ống trụ lúc này nằm ngang, trải dọc theo trục Oy. Vẽ đường tròn trên mặt phẳng Oxz rồi kéo dài theo chiều Oy.")
        if 'z=0' in eq_clean:
            items.append("<strong>Mặt phẳng đáy (z = 0):</strong> Tượng trưng cho mặt sàn Oxy, cắt phẳng phần bên dưới của khối hình.")
        if 'z=1' in eq_clean or 'z=2' in eq_clean or 'z=3' in eq_clean:
            items.append("<strong>Mặt phẳng nằm ngang (z = h):</strong> Vẽ một hình bình hành lơ lửng song song với mặt sàn ở độ cao h để cắt nắp vật thể.")
        if 'y=x' in eq_clean or 'y=2x' in eq_clean or 'x=y' in eq_clean:
            items.append("<strong>Mặt phẳng chéo (y = x):</strong> Kẻ đường y=x dưới sàn, rồi dựng một vách ngăn thẳng đứng từ đường đó lên dọc theo trục Oz.")
        if 'y=0' in eq_clean:
            items.append("<strong>Mặt xOz (y = 0):</strong> Là vách tường đi qua trục Ox và Oz, ngăn không gian làm hai nửa.")
        if 'x=0' in eq_clean:
            items.append("<strong>Mặt yOz (x = 0):</strong> Là vách tường đi qua trục Oy và Oz.")
            
        if not items:
            items.append("<strong>Phác họa khối vật thể:</strong> Bắt đầu bằng việc kẻ 3 trục vuông góc Oxyz. Ước lượng và vẽ các mặt biên giao với các trục.")
        
        items.append("<em>💡 Mẹo vẽ 3D bằng tay:</em> Hãy tìm phương trình giao tuyến của các mặt (ví dụ cho 2 giá trị z bằng nhau). Giao tuyến thường là đường tròn hoặc elip nằm lơ lửng. Vẽ giao tuyến đó bằng nét liền, còn nét đứt cho các viền bị khuất phía sau khối hình.")

    else:
        # 2D Rules
        if 'x^2+y^2' in eq_clean:
            items.append("<strong>Hình tròn (x² + y² ≤ R²):</strong> Chấm tâm tại gốc O, quay một vòng tròn bán kính R. Nếu là hình vành khăn, vẽ thêm một vòng tròn đồng tâm nhỏ hơn.")
        if 'y=x^2' in eq_clean or 'y=2x^2' in eq_clean or 'y=x^2/2' in eq_clean:
            items.append("<strong>Parabol đứng (y = ax²):</strong> Chấm đỉnh tại O(0,0), bề lõm hướng lên trên ôm lấy trục Oy. Đánh dấu điểm phụ như x=1, y=a để uốn đường cong cho chuẩn.")
        if 'x=y^2' in eq_clean or 'x=2y^2' in eq_clean or 'x=y^2/2' in eq_clean:
            items.append("<strong>Parabol ngang (x = ay²):</strong> Đỉnh nằm tại gốc O, nhưng bề lõm quay sang bên phải ôm lấy trục Ox.")
        if 'y=2-x^2' in eq_clean or 'y=4-x^2' in eq_clean:
            items.append("<strong>Parabol úp (y = a - x²):</strong> Đỉnh nằm trên trục Oy tại y=a, bề lõm uốn cong úp xuống dưới.")
        if 'y=x' in eq_clean or 'y=2x' in eq_clean:
            items.append("<strong>Đường thẳng qua gốc (y = ax):</strong> Dùng thước kẻ đường thẳng chéo đi qua gốc tọa độ và điểm (1,a).")
        if 'y=-x' in eq_clean:
            items.append("<strong>Đường thẳng (y = -x):</strong> Kẻ đường thẳng chéo từ góc phần tư thứ hai xuống góc phần tư thứ tư.")
        if 'y=0' in eq_clean:
            items.append("<strong>Trục hoành (y = 0):</strong> Là đường giới hạn bằng chính trục ngang Ox.")
        if 'x=0' in eq_clean:
            items.append("<strong>Trục tung (x = 0):</strong> Là đường giới hạn bằng chính trục dọc Oy.")
        if 'y=4' in eq_clean or 'x=1' in eq_clean or 'y=1' in eq_clean:
            items.append("<strong>Các đường thẳng song song trục:</strong> Vẽ các vạch giới hạn vuông góc với trục tại mốc tọa độ tương ứng.")
            
        if not items:
            items.append("<strong>Phác họa miền D:</strong> Kẻ trục tọa độ Oxy. Dựa vào phương trình biên để kẻ các đường giới hạn.")
            
        items.append("<em>💡 Mẹo vẽ 2D bằng tay:</em> Bước quan trọng nhất là lập phương trình hoành độ giao điểm để tìm tọa độ các góc của miền D. Chấm các giao điểm này lên trục trước, rồi dùng thước/tay nối các đường biên lại. Vùng bị khép kín chính là diện tích cần tìm.")

    for item in items:
        guide_html += f"  <li>{item}</li>\n"
        
    guide_html += "  </ul>\n</div>\n"
    return guide_html


def process_files():
    count = 0
    for prefix, total in [('B1', 20), ('B2', 22), ('B3', 15)]:
        for i in range(1, total + 1):
            fname = f"{prefix}_{i}.html"
            path = os.path.join(BASE_DIR, fname)
            if not os.path.exists(path): continue
            
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if '&#127912; Hướng dẫn chi tiết cách vẽ hình' in content:
                continue # Already processed
                
            # Find the subtitle block
            match = re.search(r'&#128208; Hình vẽ cho:\s*(.*?)</p>', content)
            if match:
                eq_text = match.group(1)
                guide = generate_drawing_guide(eq_text)
                
                # Insert right before <div class="plot-container">
                content = content.replace('<div class="plot-container">', guide + '<div class="plot-container">', 1)
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1; print(f'Processed {fname}', flush=True)
    print(f"Added drawing guides to {count} files.")

if __name__ == '__main__':
    process_files()
