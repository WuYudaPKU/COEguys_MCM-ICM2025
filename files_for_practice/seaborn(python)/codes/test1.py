import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set(style='darkgrid') # styles:darkgrid, whitegrid, dark, white, ticks
sns.set(palette='RdBu') # 改变图表颜色

# 利用pandas读文件
tips=pd.read_csv(r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\datasets\datasets\tips.csv')
# 绘图
sns.relplot(
    data=tips,
    x='total_bill',y='tip',col='time',
    hue='smoker',style='smoker',size='size'
)
# 显示
plt.show()