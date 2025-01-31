from PIL import Image
import numpy as np

# 给定的色卡
color_palette1 = [
    (169, 0, 50),   # #A90032
    (174, 41, 124), # #AE297C
    (133, 91, 188), # #855BBC
    (0, 130, 222),  # #0082DE
    (0, 158, 219),  # #009EDB
    (0, 179, 189)   # #00B3BD
]
color_palette2 = [
    (169, 0, 50),    # #A90032
    (151, 26, 90),   # #971A5A
    (117, 52, 114),  # #753472
    (78, 67, 120),   # #4E4378
    (49, 72, 108),   # #31486C
    (47, 72, 88)     # #2F4858
]
color_palette3 = [
    (169, 0, 50),    # #A90032
    (191, 165, 165), # #BFA5A5
    (137, 113, 113), # #897171
    (68, 91, 0),     # #445B00
    (121, 141, 0)    # #798D00
]
color_palette4 = [
    (169, 0, 50),    # #A90032
    (255, 159, 169), # #FF9FA9
    (0, 190, 198),   # #00BEC6
    (243, 238, 217)  # #F3EED9
]
color_science=[
    (153, 55, 153),  # #993799
    (254, 136, 0),   # #FE8800
    (50, 90, 160),   # #325AA0
    (100, 100, 100), # #646464
    (66, 153, 56),   # #429938
    (245, 113, 109), # #F5716D
    (255, 172, 96),  # #FFAC60
    (97, 172, 255)   # #61ACFF
]



# 计算渐变颜色
def generate_gradient(palette, colors_per_segment=3):
    gradient = []
    total_colors = len(palette)
    
    # 每两个相邻的颜色之间进行渐变插值
    for i in range(total_colors - 1):
        start_color = np.array(palette[i])
        end_color = np.array(palette[i + 1])
        for j in range(colors_per_segment):
            ratio = j / (colors_per_segment - 1)
            interpolated_color = np.round((1 - ratio) * start_color + ratio * end_color).astype(int)
            gradient.append(tuple(interpolated_color))
    
    return gradient

# 生成渐变色
gradient_colors = generate_gradient(color_science)

# 创建一个 16x16 像素的 BMP 图像
width, height = 16, 16
image = Image.new("RGB", (width, height))

# 将渐变色填充到图像中
pixels = image.load()
color_idx = 0
total_pixels = width * height

# 通过循环方式避免越界问题
for y in range(height):
    for x in range(width):
        pixels[x, y] = gradient_colors[color_idx % len(gradient_colors)]  # 使用余数避免越界
        color_idx += 1

# 保存为 BMP 文件
image.save("science.bmp")

print("BMP 文件已生成！")