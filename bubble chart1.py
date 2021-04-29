import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from chart_func import plot_bubble
import numpy as np
import matplotlib.font_manager as fm
from adjustText import adjust_text
import xlrd
from xlrd import open_workbook

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('bubble_chart_data.xlsx', index_col='分子名CN')

color_dict = {'缬沙坦': 'grey',
              '厄贝沙坦': 'orange',
              '氨氯地平+缬沙坦': 'navy',
              '氯沙坦': 'orange',
              '厄贝沙坦+氢氯噻嗪': 'navy',
              '奥美沙坦': 'orange',
              '培哚普利': 'grey',
              '氯沙坦+氢氯噻嗪': 'navy',
              '替米沙坦': 'grey',
              '坎地沙坦': 'orange',
              '贝那普利': 'grey',
              '缬沙坦+氢氯噻嗪': 'navy',
              '阿利沙坦': 'grey',
              '培哚普利+吲达帕胺': 'navy',
              '福辛普利': 'orange',
              '替米沙坦+氢氯噻嗪': 'navy',
              '依那普利': 'orange',
              '氨氯地平+贝那普利': 'navy',
              '奥美沙坦+氢氯噻嗪': 'navy',
              '雷米普利': 'grey',
              '咪达普利': 'grey',
              '贝那普利+氢氯噻嗪': 'navy',
              '赖诺普利+氢氯噻嗪': 'navy',
              '卡托普利': 'grey',
              '坎地沙坦+氢氯噻嗪': 'navy',
              '赖诺普利': 'orange',
              '依那普利+氢氯噻嗪': 'navy',
              '卡托普利+氢氯噻嗪': 'navy'}

x = df.iloc[1:-2, 0]
y = df.iloc[1:-2, 1]
# x.drop('阿利沙坦', inplace=True)
# y.drop('阿利沙坦', inplace=True)
z = df.iloc[1:-2, 2]/100000
labels = x.index.tolist()
avggr = df.iloc[-1, 1]
title_text = 'RAAS市场TOP15分子气泡图'


plot_bubble(x=x, y=y, z=z, labels=labels, title=title_text, xtitle='MS% in RAAS市场', ytitle='同比增长率',
            yavgline=True, yavg= avggr, ylim=[-0.5, 1], xlim=[0, 0.15])
