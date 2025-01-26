import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
x = np.linspace(0, 10, 100)  # 从 0 到 10，100 个点
y = np.sin(x)  # 对应的 y 值为 sin(x)

# 使用 seaborn 绘制平滑曲线图
sns.lineplot(x=x, y=y)

# 设置标题和标签
plt.title('Smooth Curve using Seaborn', fontsize=16)
plt.xlabel('X', fontsize=14)
plt.ylabel('Y', fontsize=14)

# 显示图形
plt.show()