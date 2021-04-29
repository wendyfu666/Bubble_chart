import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import matplotlib.font_manager as fm
import numpy as np
import types
from adjustText import adjust_text
import itertools
import matplotlib.cm as cm

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams.update({'font.size': 16})
sns.set_style("white",{"font.sans-serif":['simhei', 'Arial']})

myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

color_dict = {'拜阿司匹灵': 'navy',
              '波立维': 'crimson',
              '泰嘉': 'teal',
              '帅信': 'darkgreen',
              '帅泰': 'olivedrab',
              '倍林达': 'darkorange',
              '泰仪': 'sienna',
              '阿司匹林': 'navy',
              '氯吡格雷': 'teal',
              '替格瑞洛': 'darkorange',
              '国产阿司匹林': 'grey',
              '华东区': 'navy',
              '华西区': 'crimson',
              '华南区': 'teal',
              '华北区': 'darkgreen',
              '华中区': 'darkorange',
              '未分区': 'grey',
              '一线城市': 'navy',
              '二线城市': 'crimson',
              '三线城市': 'teal',
              '四线城市': 'darkgreen',
              '五线城市': 'darkorange',
              '25MG10片装': 'darkgreen',
              '25MG20片装': 'olivedrab',
              '75MG7片装': 'darkorange',
              '75MG20片装': 'sienna',
              '300MG7片装': 'navy',
              '300MG2片装': 'teal',
              '缬沙坦': 'grey',
              '厄贝沙坦': 'darkorange',
              '氨氯地平+缬沙坦': 'navy',
              '氯沙坦': 'darkorange',
              '厄贝沙坦+氢氯噻嗪': 'navy',
              '奥美沙坦': 'darkorange',
              '培哚普利': 'grey',
              '氯沙坦+氢氯噻嗪': 'navy',
              '替米沙坦': 'grey',
              '坎地沙坦': 'darkorange',
              '贝那普利': 'grey',
              '缬沙坦+氢氯噻嗪': 'navy',
              '阿利沙坦': 'grey',
              '培哚普利+吲达帕胺': 'navy',
              '福辛普利': 'darkorange',
              '替米沙坦+氢氯噻嗪': 'navy',
              '依那普利': 'darkorange',
              '氨氯地平+贝那普利': 'navy',
              '奥美沙坦+氢氯噻嗪': 'navy',
              '雷米普利': 'grey',
              '咪达普利': 'grey',
              '贝那普利+氢氯噻嗪': 'navy',
              '赖诺普利+氢氯噻嗪': 'navy',
              '卡托普利': 'grey',
              '坎地沙坦+氢氯噻嗪': 'navy',
              '赖诺普利': 'darkorange',
              '依那普利+氢氯噻嗪': 'navy',
              '卡托普利+氢氯噻嗪': 'navy'}


# def plot_line(df, savefile, colormap='tab10', width=12, height=5, xlabelrotation=0, ylabelperc=False,
#                    title='', xtitle='', ytitle=''):
#
#     # Choose seaborn style
#     sns.set_style("white")
#
#     # Create a color palette
#     #palette = plt.get_cmap(colormap)
#
#     # prepare the plot and its size
#     fig, ax = plt.subplots()
#     fig.set_size_inches(width, height)
#
#     # Generate the lines
#     count = 0
#     for column in df:
#         markerstyle = 'o'
#         if column == '泰嘉':
#             markerstyle = 'D'
#
#         plt.plot(df.index, df[column], color=color_dict[column], linewidth=2, label=column,
#                  marker=markerstyle, markersize=5, markerfacecolor='white', markeredgecolor=color_dict[column])
#
#         endpoint = -1
#         while isinstance(df.values[endpoint][count], str) or df.values[endpoint][count]==float("inf"):
#             endpoint = endpoint - 1
#             if abs(endpoint) == len(df.index):
#                 break
#         if abs(endpoint) < len(df.index):
#             if df.values[endpoint][count] <= 3:
#                 plt.text(df.index[endpoint], df.values[endpoint][count], "{:.1%}".format(df.values[endpoint][count]),
#                              ha='left', va='center', size='small', color=color_dict[column])
#
#         startpoint = 0
#         while isinstance(df.values[startpoint][count], str) or df.values[startpoint][count]==float("inf"):
#             startpoint = startpoint + 1
#             if startpoint == len(df.index):
#                 break
#
#         if startpoint < len(df.index):
#             if df.values[startpoint][count] <= 3:
#                 plt.text(df.index[startpoint], df.values[startpoint][count], "{:.1%}".format(df.values[startpoint][count]),
#                              ha='right', va='center', size='small', color=color_dict[column])
#         count += 1
#
#     # Customize the major grid
#     plt.grid(which='major', linestyle=':', linewidth='0.5', color='grey')
#
#     # Rotate labels in X axis as there are too many
#     plt.setp(ax.get_xticklabels(), rotation=xlabelrotation, horizontalalignment='center')
#
#     # Change the format of Y axis to 'x%'
#     if ylabelperc == True:
#         ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
#
#     # Add titles
#     plt.title(title, fontproperties=myfont, fontsize=18)
#     plt.xlabel(xtitle, fontproperties=myfont)
#     plt.ylabel(ytitle,fontproperties=myfont)
#
#     # Shrink current axis by 20% and put a legend to the right of the current axis
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
#     ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), labelspacing=1.5, prop={'family':'SimHei'})
#
#     ymax = ax.get_ylim()[1]
#     if ymax > 3:
#         ax.set_ylim(ymax=3)
#
#     # Save the figure
#     plt.savefig(savefile, format='png', bbox_inches='tight', dpi=600)
#
#     #Close
#     plt.clf()
#     plt.cla()
#     plt.close()

# def plot_pie(sizelist, labellist, savefile, width=6, height=6, title=None):
#
#     sns.set_style("white")
#
#     #Prepare the white center circle for Donat shape
#     my_circle = plt.Circle((0, 0), 0.7, color='white')
#
#     sizelist = sizelist.transform(lambda x: x/x.sum())
#     print(sizelist)
#     sizelist_mask = []
#     for size in sizelist:
#         sizelist_mask.append(abs(size))
#
#     #Draw the pie chart
#     wedges, texts, autotexts = plt.pie(sizelist_mask, labels=labellist, autopct='%1.1f%%', pctdistance=0.85,
#                               wedgeprops={'linewidth': 3, 'edgecolor': 'white'},
#                               textprops={'family': 'Simhei'})
#
#     for i, pie_wedge in enumerate(wedges):
#         pie_wedge.set_facecolor(color_dict[pie_wedge.get_label()])
#
#         if pie_wedge.get_label() == '泰嘉':
#             pie_wedge.set_hatch('//')
#         if sizelist[i] < 0:
#             pie_wedge.set_facecolor('white')
#
#     for i, autotext in enumerate(autotexts):
#         autotext.set_color('white')
#         autotext.set_fontsize(10)
#         autotext.set_text("{:.1%}".format(sizelist[i]))
#         if sizelist[i] < 0:
#             autotext.set_color('r')
#
#     #Add title at the center
#     plt.text(0, 0, title, horizontalalignment='center', verticalalignment='center', size=20, fontproperties=myfont)
#
#     #Combine circle part and pie part
#     fig = plt.gcf()
#     fig.set_size_inches(width, height)
#     fig.gca().add_artist(my_circle)
#
#     #Save
#     plt.savefig(savefile, format='png', bbox_inches='tight', dpi=600)
#
#     #Close
#     plt.clf()
#     plt.cla()
#     plt.close()



# def plot_bubble_m(x, y, z, avggr, labels, savefile, width=12, height=5, xfmt='{:.0%}', yfmt='{:+.0%}', ylabel='市场平均\n增长率',
#                 xavgline=False, avgms=None, title=None, xtitle=None, ytitle=None):
#     fig, ax = plt.subplots()
#     fig.set_size_inches(width, height)
#
#     colors = iter(cm.rainbow(np.linspace(0, 1, len(y))))
#
#     ax.axhline(avggr, linestyle='--', linewidth=1, color='r')
#     if xavgline==True:
#         ax.axvline(avgms,linestyle='--', linewidth=1, color='r')
#     for i in range(len(x)):
#         ax.scatter(x[i], y[i], z[i], color=next(colors), alpha=0.6, edgecolors="black")
#     # ax.scatter(x, y, s=z, c=color, alpha=0.6, edgecolors="grey")
#     #ax.grid(which='major', linestyle=':', linewidth='0.5', color='black')
#
#     ax.xaxis.set_major_formatter(FuncFormatter(lambda y, _: xfmt.format(y)))
#     ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: yfmt.format(y)))
#
#     np.random.seed(0)
#     # for i, txt in enumerate(labels):
#     #     text = plt.text(x[i],y[i], txt+"\n"+ '('+ str("{:.1%}".format(x[i])) +', ' + str("{:.1%}".format(y[i])) + ')', ha='center', va='center')
#     texts = [plt.text(x[i], y[i], labels[i],
#                       ha='center', va='center', multialignment='center', fontproperties=myfont, fontsize=10) for i in range(len(labels))]
#     adjust_text(texts, arrowprops=dict(arrowstyle='->', color='black'))
#     plt.text(ax.get_xlim()[1],avggr, ylabel+':\n'+yfmt.format(avggr), ha='left', va='center', color='r', multialignment='center' , fontproperties=myfont, fontsize=10)
#     if xavgline==True:
#         plt.text(avgms, ax.get_ylim()[1], '全国平均\n份额:\n' + xfmt.format(avgms), ha='left', va='top',
#                  color='r', multialignment='center', fontproperties=myfont, fontsize=10)
#
#     plt.title(title, fontproperties=myfont, fontsize=18)
#     plt.xlabel(xtitle, fontproperties=myfont)
#     plt.ylabel(ytitle, fontproperties=myfont)
#
#     # Save
#     plt.savefig(savefile, format='png', bbox_inches='tight', dpi=600)
#
#     # Close
#     plt.clf()
#     plt.cla()
#     plt.close()

# def plot_bubble(x, y, z, avggr, labels, savefile, width=12, height=5, xfmt='{:.1%}', yfmt='{:+.1%}', ylabel='市场平均\n增长率',
#                 xavgline=False, avgms=None, title=None, xtitle=None, ytitle=None):
#     fig, ax = plt.subplots()
#     fig.set_size_inches(width, height)
#
#     ax.axhline(avggr, linestyle='--', linewidth=1, color='r')
#     if xavgline==True:
#         ax.axvline(avgms,linestyle='--', linewidth=1, color='r')
#     for i in range(len(x)):
#         ax.scatter(x[i], y[i], z[i], color=color_dict[labels[i]], alpha=0.6, edgecolors="black")
#     # ax.scatter(x, y, s=z, c=color, alpha=0.6, edgecolors="grey")
#     #ax.grid(which='major', linestyle=':', linewidth='0.5', color='black')
#
#     ax.xaxis.set_major_formatter(FuncFormatter(lambda y, _: xfmt.format(y)))
#     ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: yfmt.format(y)))
#
#     np.random.seed(0)
#     # for i, txt in enumerate(labels):
#     #     text = plt.text(x[i],y[i], txt+"\n"+ '('+ str("{:.1%}".format(x[i])) +', ' + str("{:.1%}".format(y[i])) + ')', ha='center', va='center')
#     texts = [plt.text(x[i], y[i], labels[i]+"\n"+ '('+ str(xfmt.format(x[i])) +', ' + str(yfmt.format(y[i])) + ')',
#                       ha='center', va='center', multialignment='center', fontproperties=myfont, fontsize=14) for i in range(len(labels))]
#     adjust_text(texts, arrowprops=dict(arrowstyle='->', color='black'))
#     plt.text(ax.get_xlim()[1],avggr, ylabel+':\n'+yfmt.format(avggr), ha='left', va='center', color='r', multialignment='center', fontproperties=myfont, fontsize=14)
#     if xavgline==True:
#         plt.text(avgms, ax.get_ylim()[1], '全国平均\n份额:\n' + xfmt.format(avgms), ha='left', va='top',
#                  color='r', multialignment='center', fontproperties=myfont, fontsize=14)
#
#     plt.title(title, fontproperties=myfont, fontsize=18)
#     plt.xlabel(xtitle, fontproperties=myfont)
#     plt.ylabel(ytitle, fontproperties=myfont)
#
#     # Save
#     plt.savefig(savefile, format='png', bbox_inches='tight', dpi=600)
#
#     # Close
#     plt.clf()
#     plt.cla()
#     plt.close()

def plot_bubble(x, y, z, labels, title, xtitle, ytitle, xfmt='{:.0%}', yfmt='{:+.0%}',
                yavgline=False, yavg=None, ylabel='', xavgline=False, xavg=None, xlabel='',
                ylim=None, xlim=None, yunit=None, xunit=None, showLabel=True, labelLimit=15):
    # y_unit_label = change_unit(unit=yunit, text_sign=ytitle[-1], df=y)[0]
    # y = change_unit(unit=yunit, text_sign=ytitle[-1], df=y)[1]
    # x_unit_label = change_unit(unit=xunit, text_sign=xtitle[-1], df=x)[0]
    # x = change_unit(unit=xunit, text_sign=xtitle[-1], df=x)[1]

    fig, ax = plt.subplots()
    fig.set_size_inches(14, 7)

    if ylim is not None:
        ax.set_ylim(ymin=ylim[0], ymax=ylim[1])
    if xlim is not None:
        ax.set_xlim(xmin=xlim[0], xmax=xlim[1])

    for col in df.index:
        if col in color_dict.keys():
            color = color_dict[col]
        else:
            color = color_list[i]

    # cmap = mpl.colors.ListedColormap(np.random.rand(256, 3))
    # colors = iter(cmap(np.linspace(0, 1, len(y))))

    for i in range(len(x)):
        ax.scatter(x[i], y[i], z[i], color=next(colors), alpha=0.6, edgecolors="black")
    if yavgline == True:
        ax.axhline(yavg, linestyle='--', linewidth=1, color='r')
    if xavgline == True:
        ax.axvline(xavg, linestyle='--', linewidth=1, color='r')
    ax.scatter(x, y, s=z, c=color, alpha=0.6, edgecolors="grey")
    ax.grid(which='major', linestyle=':', linewidth='0.5', color='black')

    ax.xaxis.set_major_formatter(FuncFormatter(lambda y, _: xfmt.format(y)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: yfmt.format(y)))

    np.random.seed(0)
    # for i, txt in enumerate(labels):
    #     text = plt.text(x[i],y[i], txt+"\n"+ '('+ str("{:.1%}".format(x[i])) +', ' + str("{:.1%}".format(y[i])) + ')', ha='center', va='center')
    if showLabel is True:
        texts = [plt.text(x[i], y[i], labels[i],
                          ha='center', va='center', multialignment='center', fontproperties=myfont, fontsize=10) for i
                 in range(len(labels[:labelLimit]))]
        adjust_text(texts, force_text=0.01, arrowprops=dict(arrowstyle='->', color='black'))

    if yavgline == True:
        plt.text(ax.get_xlim()[1], yavg, ylabel, ha='left', va='center', color='r', multialignment='center',
                 fontproperties=myfont, fontsize=10)
    if xavgline == True:
        plt.text(xavg, ax.get_ylim()[1], xlabel, ha='left', va='top',
                 color='r', multialignment='center', fontproperties=myfont, fontsize=10)

    plt.title(title, fontproperties=myfont)
    # plt.xlabel(xtitle + x_unit_label, fontproperties=myfont, fontsize=12)
    # plt.ylabel(ytitle + y_unit_label, fontproperties=myfont, fontsize=12)

    # Save
    plt.savefig('plots/' + title + '.png', format='png', bbox_inches='tight', transparent=True, dpi=600)
    print('plots/' + title + '.png saved...')

    # Close
    plt.clf()
    plt.cla()
    plt.close()

# def plot_dual_line(df1, df2, savefile, colormap='tab10', width=15, height=6, xlabelrotation=0,
#                    title1='', xtitle1='', ytitle1='', title2='', xtitle2='', ytitle2=''):
#
#     # Choose seaborn style
#     sns.set_style("white")
#
#     # Create a color palette
#     #palette = plt.get_cmap(colormap)
#
#     # prepare the plot and its size
#     fig = plt.figure(figsize=(width, height), facecolor='white')
#
#     # Generate the lines of df1
#     ax = plt.subplot(1, 2, 1)
#     count = 0
#     for column in df1:
#         markerstyle = 'o'
#         if column == '泰嘉':
#             markerstyle = 'D'
#
#         plt.plot(df1.index, df1[column], color=color_dict[column], linewidth=2, label=column,
#                  marker=markerstyle, markersize=5, markerfacecolor='white', markeredgecolor=color_dict[column])
#
#         endpoint = -1
#         while np.isnan(df1.values[endpoint][count])  or df1.values[endpoint][count]==float("inf"):
#             endpoint = endpoint - 1
#             if abs(endpoint) == len(df1.index):
#                 break
#         if abs(endpoint) < len(df1.index):
#             if df1.values[endpoint][count] <= 3:
#                 plt.text(df1.index[endpoint], df1.values[endpoint][count], "{:.1%}".format(df1.values[endpoint][count]),
#                              ha='left', va='center', size='small', color=color_dict[column])
#
#         startpoint = 0
#         while np.isnan(df1.values[startpoint][count]) or df1.values[startpoint][count]==float("inf"):
#             startpoint = startpoint + 1
#             if startpoint == len(df1.index):
#                 break
#
#         if startpoint < len(df1.index):
#             if df1.values[startpoint][count] <= 3:
#                 plt.text(df1.index[startpoint], df1.values[startpoint][count], "{:.1%}".format(df1.values[startpoint][count]),
#                              ha='right',va='center', size='small', color=color_dict[column])
#         count += 1
#
#     # Customize the major grid
#     plt.grid(which='major', linestyle=':', linewidth='0.5', color='grey')
#
#     # Rotate labels in X axis as there are too many
#     plt.setp(ax.get_xticklabels(), rotation=xlabelrotation, horizontalalignment='center')
#
#     # Change the format of Y axis to 'x%'
#     ax.yaxis.set_major_formatter(plt.NullFormatter())
#
#     # Add titles
#     plt.title(title1, fontproperties=myfont, fontsize=18)
#     plt.xlabel(xtitle1, fontproperties=myfont)
#     plt.ylabel(ytitle1,fontproperties=myfont)
#
#     ax = plt.subplot(1, 2, 2)
#     count = 0
#     for column in df2:
#         markerstyle = 'o'
#         if column == '泰嘉':
#             markerstyle = 'D'
#
#         plt.plot(df2.index, df2[column], color=color_dict[column], linewidth=2, label=column,
#                  marker=markerstyle, markersize=5, markerfacecolor='white', markeredgecolor=color_dict[column])
#
#         endpoint = -1
#         while np.isnan(df2.values[endpoint][count])  or df2.values[endpoint][count]==float("inf"):
#             endpoint = endpoint - 1
#             if abs(endpoint) == len(df2.index):
#                 break
#         if abs(endpoint) < len(df2.index):
#             if df2.values[endpoint][count] <= 3:
#                 plt.text(df2.index[endpoint], df2.values[endpoint][count], "{:+.1%}".format(df2.values[endpoint][count]),
#                              ha='left', va='center', size='small', color=color_dict[column])
#
#         startpoint = 0
#         while np.isnan(df2.values[startpoint][count])  or df2.values[startpoint][count]==float("inf"):
#             startpoint = startpoint + 1
#             if startpoint == len(df2.index):
#                 break
#
#         if startpoint < len(df2.index):
#             if df2.values[startpoint][count] <= 3:
#                 plt.text(df2.index[startpoint], df2.values[startpoint][count], "{:+.1%}".format(df2.values[startpoint][count]),
#                              ha='right', va='center', size='small', color=color_dict[column])
#         count += 1
#
#     # Customize the major grid
#     plt.grid(which='major', linestyle=':', linewidth='0.5', color='grey')
#
#     # Rotate labels in X axis as there are too many
#     plt.setp(ax.get_xticklabels(), rotation=xlabelrotation, horizontalalignment='center')
#
#     # Change the format of Y axis to 'x%'
#     ax.yaxis.set_major_formatter(plt.NullFormatter())
#
#     # Add titles
#     plt.title(title2, fontproperties=myfont, fontsize=18)
#     plt.xlabel(xtitle2, fontproperties=myfont)
#     plt.ylabel(ytitle2,fontproperties=myfont)
#
#     # Shrink current axis by 20% and put a legend to the right of the current axis
#     # box = ax.get_position()
#     # ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
#     ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), labelspacing=1.5, prop={'family':'SimHei'})
#
#     ymax = ax.get_ylim()[1]
#     if ymax > 3:
#         ax.set_ylim(ymin=-1, ymax=3)
#
#     # Save the figure
#     plt.savefig(savefile, format='png', bbox_inches='tight', dpi=600)
#
#     #Close
#     plt.clf()
#     plt.cla()
#     plt.close()


# def plot_barh(df, savefile, stacked=True, width=15, height=9, xfmt='{:.0f}', yfmt='{:.0%}', labelfmt ='{:.0%}',
#                   title=None, xtitle=None, ytitle=None, ymin=None, ymax=None,color_dict=None, haslegend=True):
#
#
#     ax = df.plot(kind='barh', stacked=stacked, figsize=(width, height), alpha=0.8, edgecolor='black', color=['darkgreen','olivedrab','darkorange'])#['navy','darkgreen','teal', 'crimson', 'grey']
#     plt.title(title, fontproperties=myfont, fontsize=18)
#     plt.xlabel(xtitle, fontproperties=myfont)
#     plt.ylabel(ytitle, fontproperties=myfont)
#     plt.axvline(x=0, linewidth=2, color='r')
#
#     if haslegend == True:
#         plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), prop=myfont, fontsize=12)
#     else:
#         plt.legend(prop=myfont)
#
#     # plt.setp(ax.get_xticklabels(), rotation=0, horizontalalignment='center')
#     #
#     # ax.xaxis.set_major_formatter(FuncFormatter(lambda y, _: xfmt.format(y)))
#     ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: yfmt.format(y)))
#     # ax.set_ylim([ymin, ymax])
#
#     # Add value label
#     labels = []
#     for j in df.columns:
#         for i in df.index:
#             label = str(df.loc[i][j])
#             labels.append(label)
#
#     patches = ax.patches
#
#     for label, rect in zip(labels, patches):
#         height = rect.get_height()
#         if height > 0.015:
#             x = rect.get_x()
#             y = rect.get_y()
#             width = rect.get_width()
#             if abs(width) < 3000000:
#                 color = 'black'
#             else:
#                 color = 'white'
#             ax.text(x + width / 2., y + height / 2., labelfmt.format(float(label)), ha='center',
#                     va='center', color=color, fontproperties=myfont, fontsize=10)
#
#     # Save the figure
#     plt.savefig(savefile, format='png', bbox_inches='tight', transparent=True, dpi=600)
#
#     # Close
#     plt.clf()
#     plt.cla()
#     plt.close()