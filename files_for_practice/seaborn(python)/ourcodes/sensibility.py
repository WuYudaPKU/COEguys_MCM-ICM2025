import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv(r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\ourcodes\sensibility\change_noise.csv', header=None)

# 设置列名
df.columns = ['0.1', '0.05', '0']

# 绘制折线图
plt.figure(figsize=(12, 8))
sns.lineplot(data=df)

# 设置标题和标签
plt.title('Change Noise Over Time', fontsize=30)
plt.xlabel('Time', fontsize=25)
plt.ylabel('Value', fontsize=25)

# 调整坐标轴刻度和标签的字体大小
plt.tick_params(axis='both', which='major', labelsize=20)

# 显示图形
plt.show()
