# -*- coding: utf-8 -*-
import os, json
import numpy as np

def inject_cylinder(filepath, trace_dict):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    idx = text.find("Plotly.newPlot(")
    if idx == -1: return False
    comma_idx = text.find(",", idx)
    bracket_idx = text.find("[", comma_idx)

    count = 0
    end_idx = -1
    in_string = False
    escape = False
    for i in range(bracket_idx, len(text)):
        char = text[i]
        if escape:
            escape = False
            continue
        if char == '\\': escape = True
        elif char == '"': in_string = not in_string
        elif not in_string:
            if char == '[': count += 1
            elif char == ']': count -= 1
            if count == 0:
                end_idx = i
                break

    if end_idx != -1:
        data_str = text[bracket_idx:end_idx+1]
        data = json.loads(data_str)
        
        # Check if already injected
        if any(t.get('name') == trace_dict['name'] for t in data):
            print(f"Already injected into {filepath}")
            return True
            
        data.append(trace_dict)
        new_data_str = json.dumps(data)
        
        new_text = text[:bracket_idx] + new_data_str + text[end_idx+1:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Injected into {filepath}")
        return True
    return False

def get_vertical_cylinder():
    theta = np.linspace(0, 2*np.pi, 60)
    z_val = np.linspace(0, 3, 20)
    theta, z_val = np.meshgrid(theta, z_val)
    return {
        "type": "surface",
        "x": np.cos(theta).tolist(),
        "y": np.sin(theta).tolist(),
        "z": z_val.tolist(),
        "colorscale": "Blues",
        "showscale": False,
        "opacity": 0.5,
        "name": "Mặt trụ"
    }

def get_horizontal_cylinder():
    u = np.linspace(0, 2*np.pi, 60)
    t = np.linspace(0, 1, 20)
    u, t = np.meshgrid(u, t)
    
    Z = np.sin(u)
    X = np.cos(u)
    Y = t * (2 - Z)
    
    return {
        "type": "surface",
        "x": X.tolist(),
        "y": Y.tolist(),
        "z": Z.tolist(),
        "colorscale": "Reds",
        "showscale": False,
        "opacity": 0.5,
        "name": "Mặt trụ"
    }

if __name__ == "__main__":
    base_dir = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"
    
    inject_cylinder(os.path.join(base_dir, "B3_11.html"), get_vertical_cylinder())
    inject_cylinder(os.path.join(base_dir, "B3_14.html"), get_vertical_cylinder())
    inject_cylinder(os.path.join(base_dir, "B3_4.html"), get_horizontal_cylinder())
