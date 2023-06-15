from PIL import Image
import numpy as np
from collections import Counter


def extract_colors(image_path):
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)
    reshaped_array = image_array.reshape(-1, 3)
    hex_colors = [f"#{''.join(f'{c:02x}' for c in color)}" for color in reshaped_array]

    # Remove black and white colors
    hex_colors = [color for color in hex_colors if not is_black_or_white(color)]

    color_counter = Counter(hex_colors)
    top_colors = color_counter.most_common(10)
    return dict(top_colors)


def is_black_or_white(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    # Check if the color is close to pure black or pure white
    return (r < 20 and g < 20 and b < 20) or (r > 235 and g > 235 and b > 235)


def hex_to_rgb(hex_color):
    hex_color = hex_color.strip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return r, g, b
