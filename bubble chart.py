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

def plot_bubble(x, #x轴的值
                y, #Y轴的值
                z, #气泡大小
                labels, #每个气泡的标签
                title, #图表的标题
                xtitle, #X轴的标题
                ytitle, #y轴的标题
                xfmt='{:.0%}', #x标签格式百分数保留一位小数
                yfmt='{:+.0%}', #y签格式百分数保留一位小数
                yavgline=False, #Y轴平均线
                yavg=None, #Y轴平均线的位置
                ylabel='', #平均线的标签
                xavgline=False, xavg=None, xlabel='',
                ylim=None, #Y轴的最大最小值，用[a，b]设置
                xlim=None,
                yunit=None, #Y轴的单位
                xunit=None,
                showLabel=True, #是否显示标签
                labelLimit=15):

    fig, ax = plt.subplots() #设置画布
    fig.set_size_inches(14, 7) #设置画布尺寸

    if ylim is not None:
        ax.set_ylim(ymin=ylim[0], ymax=ylim[1])  #如果ylim不为None，则ax.set_ylim()函数的两个参数为，ymin=ylim[0]....
    if xlim is not None:
        ax.set_xlim(xmin=xlim[0], xmax=xlim[1])

    for i in range(len(x)):  #len(x),数一下有多少个气泡，for 循环
        ax.scatter(x[i], y[i], z[i], color=color_dict[labels[i]], alpha=0.6, edgecolors="black")
        #在ax画布上画散点图，labels[i]取出的是i对应的产品名，然后color_dict[labels[i]]取出该产品对应的颜色
    if yavgline == True:
        ax.axhline(yavg, linestyle='--', linewidth=1, color='r')
        #axhline（）函数，画一条水平线函数
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


x = df.iloc[1:17, 0]
y = df.iloc[1:17, 1]
# x.drop('阿利沙坦', inplace=True)
# y.drop('阿利沙坦', inplace=True)
z = df.iloc[1:-2, 2]/100000
labels = x.index.tolist()    #tolist()函数将数组变成列表
avggr = df.iloc[-1, 1]
ylabel = 'RAAS市场平均增长率：'+ str(avggr)
title_text = 'RAAS市场TOP15分子气泡图'


plot_bubble(x=x, y=y, z=z, labels=labels, title=title_text, xtitle='MS% in RAAS市场', ytitle='同比增长率',
            yavgline=True, yavg= avggr, ylim=[-0.5, 1], xlim=[0, 0.15], labelLimit=30)
