# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib
import csv, sys
import numpy as np

nome_ficheiro = 'geoMap.csv'

palmeiras = []
corinthians = []
saopaulo = []
estados = []


with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
    reader = csv.reader(ficheiro)
    try:
        for linha in reader:
            estados.append(linha[0])
            palmeiras.append(int(linha[1].replace("%", "")))
            corinthians.append(int(linha[2].replace("%","")))
            saopaulo.append(int(linha[3].replace("%","")))

    except csv.Error as e:
        sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))

plt.rcParams.update({'font.size': 8})

ind = np.arange(len(estados)) # the x locations for the groups
width = 0.3  # the width of the bars

fig, ax = plt.subplots()
bpal = ax.bar(ind - width, palmeiras, width, yerr=0.1, label='Palmeiras', color="#b3d2bb")
bcor = ax.bar(ind, corinthians, width, yerr=0.1, label='Corinthians', color="#787878")
bsao = ax.bar(ind + width, saopaulo, width, yerr=0.1, label='São Paulo', color="#f49d9d")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentual de visitas (%)')
ax.set_xlabel('Estados (siglas)')
ax.set_title('Visitas do time por estado (17/05/2014 – 17/05/2019)')
ax.set_xticks(ind)
ax.set_xticklabels((estados))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos] * 3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


autolabel(bpal, "center")
autolabel(bcor, "center")
autolabel(bsao, "center")

fig.tight_layout()

plt.show()





