"""
箱形图（Box-plot）又称为盒须图、盒式图或箱线图，是一种用作显示一组数据分散情况资料的统计图。
它主要用于反映原始数据分布的特征，还可以进行多组数据分布特征的比较。
箱线图的绘制方法是：
先找出一组数据的最大值、最小值、中位数和两个四分位数；
然后， 连接两个四分位数画出箱子；
再将最大值和最小值与箱子相连接，中位数在箱子中间。
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid',color_codes=True) # styles:darkgrid, whitegrid, dark, white, ticks
tips=pd.read_csv(r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\datasets\datasets\tips.csv')

sns.boxplot(x='day',y='total_bill',data=tips,hue='time')
plt.show()