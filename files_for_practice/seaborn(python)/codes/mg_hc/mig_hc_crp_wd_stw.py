import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
# ...existing code...

# 设置全局字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

sns.set(style='whitegrid')
# 读取 CSV 文件
file_path = r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\codes\mig_herb.csv'  # 更新文件路径
data = pd.read_csv(file_path)

# 检查数据的前几行，确保读取正确
print(data.head())

color_science = [
    (153, 55, 153),   # #993799
    (254, 136, 0),    # #FE8800
    (50, 90, 160),    # #325AA0
    (100, 100, 100),  # #646464
    (66, 153, 56),    # #429938
    (245, 113, 109),  # #F5716D
    (255, 172, 96),   # #FFAC60
    (97, 172, 255)    # #61ACFF
]

# 将 RGB 颜色转换为 [0, 1] 范围
color_science_normalized = [np.array(color) / 255.0 for color in color_science]

# 假设每一行代表一个时间点
time = np.arange(len(data))

# 将数据从克转换为千克
# data['rice'] = data['rice'] / 1000
# data['weed'] = data['weed'] / 1000
# data['straw'] = data['straw'] / 1000

# 创建平滑曲线函数
def smooth_curve(x, y, points=500):
    x_smooth = np.linspace(x.min(), x.max(), points)
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_smooth)
    return x_smooth, y_smooth

# 创建图形并绘制 rice, weed 和 straw
plt.figure(figsize=(10, 8))
x_smooth, y_smooth = smooth_curve(time, data['rice'])
sns.lineplot(x=x_smooth, y=y_smooth, label='rice', color=color_science_normalized[0], linewidth=5)
x_smooth, y_smooth = smooth_curve(time, data['weed'])
sns.lineplot(x=x_smooth, y=y_smooth, label='weed', color=color_science_normalized[4], linewidth=3)
x_smooth, y_smooth = smooth_curve(time, data['straw'])
sns.lineplot(x=x_smooth, y=y_smooth, label='straw', color=color_science_normalized[5], linewidth=3)
plt.title('Rice, Weed and Straw Biomass Over Time', fontsize=30)
plt.xlabel('Time', fontsize=25)
plt.ylabel('Biomass (g)', fontsize=25)  # 修改单位为 kg
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend(title='Populations', fontsize=25, title_fontsize=28, loc='best')  # 将图例放在合适位置
for spine in plt.gca().spines:
    plt.gca().spines[spine].set_visible(True)
    plt.gca().spines[spine].set_color('black')
    plt.gca().spines[spine].set_linewidth(2)
plt.tight_layout()
plt.show()