import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.font_manager as fm
from adjustText import adjust_text
import xlrd
from xlrd import open_workbook

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('bubble_chart_data.xlsx', index_col='分子名CN')
df1= pd.read_excel('bubble_chart_data.xlsx')
# print(df)

df2= df1.iloc[:-2, 0]

myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
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

def plot_bubble(x, y, z, labels, title, xtitle, ytitle, xfmt='{:.0%}', yfmt='{:+.0%}',
                yavgline=False, yavg=None, ylabel='', xavgline=False, xavg=None, xlabel='',
                ylim=None, xlim=None, yunit=None, xunit=None, showLabel=True, labelLimit=15):

    fig, ax = plt.subplots()
    fig.set_size_inches(14, 7)

    if ylim is not None:
        ax.set_ylim(ymin=ylim[0], ymax=ylim[1])
    if xlim is not None:
        ax.set_xlim(xmin=xlim[0], xmax=xlim[1])

    for i in range(len(x)):
        ax.scatter(x[i], y[i], z[i], color=color_dict[labels[i]], alpha=0.6, edgecolors="black")
    if yavgline == True:
        ax.axhline(yavg, linestyle='--', linewidth=1, color='r')
    if xavgline == True:
        ax.axvline(xavg, linestyle='--', linewidth=1, color='r')
    # ax.scatter(x, y, s=z, c='red', alpha=0.6, edgecolors="grey")
    ax.grid(which='major', linestyle=':', linewidth=0.5, color='black')

    # ax.xaxis.set_major_formatter(FuncFormatter(lambda y, _: xfmt.format(y)))
    # ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: yfmt.format(y)))

    # np.random.seed(0)
    # for i, txt in enumerate(labels):
    # text = plt.text(x[i],y[i], txt+"\n"+ '('+ str("{:.1%}".format(x[i])) +', ' + str("{:.1%}".format(y[i])) + ')', ha='center', va='center')
    if showLabel is True:
        texts = [plt.text(x[i], y[i], labels[i], ha='center', va='center', multialignment='center', fontproperties=myfont, fontsize=10)
                 for i in range(len(labels[:labelLimit]))]
        adjust_text(texts, force_text=0.01, arrowprops=dict(arrowstyle='->', color='black'))

    if yavgline == True:
        plt.text(ax.get_xlim()[1], yavg, ylabel, ha='left', va='center', color='r', multialignment='center',
                 fontproperties=myfont, fontsize=10)
    if xavgline == True:
        plt.text(xavg, ax.get_ylim()[1], xlabel, ha='left', va='top',
                 color='r', multialignment='center', fontproperties=myfont, fontsize=10)

    plt.title(title, fontproperties=myfont)
    plt.xlabel(xtitle + x_unit_label, fontproperties=myfont, fontsize=12)
    plt.ylabel(ytitle + y_unit_label, fontproperties=myfont, fontsize=12)

    # plt.show()
    # plt.savefig(title + '.png')

    # Save
    plt.savefig('plots/' + title + '.png', format='png', bbox_inches='tight', transparent=True, dpi=600)
    print('plots/' + title + '.png saved...')

    # Close
    plt.clf()
    plt.cla()
    plt.close()


x = df.iloc[1:-2, 0]
y = df.iloc[1:-2, 1]
# x.drop('阿利沙坦', inplace=True)
# y.drop('阿利沙坦', inplace=True)
z = df.iloc[1:-2, 2]/100000
labels = x.index.tolist()
avggr = df.iloc[-1, 1]
ylabel = 'RAAS市场平均增长率：'+ str(avggr)
title_text = 'RAAS市场TOP15分子气泡图'


plot_bubble(x=x, y=y, z=z, labels=labels, title=title_text, xtitle='MS% in RAAS市场', ytitle='同比增长率',
            yavgline=True, yavg= avggr, ylim=[-0.5, 1], xlim=[0, 0.15], labelLimit=30)
