data = {}

data["ground"] = {}
data["ground"]["GALE"]={"hv":100, "spread":100}
data["ground"]["NSGAII"]={"hv":204, "spread":169}
data["ground"]["SPEA2"]={"hv":204, "spread":180}
data["ground"]["GALE_NM"]={"hv":157, "spread":126}
data["ground"]["GALE_LP"]={"hv":195, "spread":169}


data["POM3A"] = {}
data["POM3A"]["GALE"]={"hv":99.91, "spread":99}
data["POM3A"]["NSGAII"]={"hv":106, "spread":151}
data["POM3A"]["SPEA2"]={"hv":106, "spread":156}
data["POM3A"]["GALE_NM"]={"hv":101, "spread":91}
data["POM3A"]["GALE_LP"]={"hv":104, "spread":104}

data["POM3B"] = {}
data["POM3B"]["GALE"]={"hv":94, "spread":93}
data["POM3B"]["NSGAII"]={"hv":201, "spread":135}
data["POM3B"]["SPEA2"]={"hv":184, "spread":143}
data["POM3B"]["GALE_NM"]={"hv":91, "spread":126}
data["POM3B"]["GALE_LP"]={"hv":137, "spread":102}

data["POM3C"] = {}
data["POM3C"]["GALE"]={"hv":99, "spread":99}
data["POM3C"]["NSGAII"]={"hv":105, "spread":112}
data["POM3C"]["SPEA2"]={"hv":104, "spread":128}
data["POM3C"]["GALE_NM"]={"hv":100, "spread":84}
data["POM3C"]["GALE_LP"]={"hv":103, "spread":75}


data["XOMO_OSP"] = {}
data["XOMO_OSP"]["GALE"]={"hv":100, "spread":100}
data["XOMO_OSP"]["NSGAII"]={"hv":260, "spread":155}
data["XOMO_OSP"]["SPEA2"]={"hv":260, "spread":152}
data["XOMO_OSP"]["GALE_NM"]={"hv":148, "spread":88}
data["XOMO_OSP"]["GALE_LP"]={"hv":245, "spread":152}

data["XOMOO2"] = {}
data["XOMOO2"]["GALE"]={"hv":100, "spread":100}
data["XOMOO2"]["NSGAII"]={"hv":171, "spread":355}
data["XOMOO2"]["SPEA2"]={"hv":171, "spread":311}
data["XOMOO2"]["GALE_NM"]={"hv":101, "spread":210}
data["XOMOO2"]["GALE_LP"]={"hv":163, "spread":281}

data["XOMO_Flight"] = {}
data["XOMO_Flight"]["GALE"]={"hv":100, "spread":100}
data["XOMO_Flight"]["NSGAII"]={"hv":147, "spread":143}
data["XOMO_Flight"]["SPEA2"]={"hv":147, "spread":144}
data["XOMO_Flight"]["GALE_NM"]={"hv":100, "spread":130}
data["XOMO_Flight"]["GALE_LP"]={"hv":140, "spread":131}

import numpy as np
import matplotlib.pyplot as plt



def get_data(method, field):
    datasets = ["POM3A", "POM3B", "POM3C", "XOMO_OSP", "XOMOO2", "ground", "XOMO_Flight"]
    return_arr = []
    for dataset in datasets:
        return_arr.append(data[dataset][method][field])
    return return_arr

# index = np.array([10, 40, 70, 100, 130, 160])
index = np.array([30*(i+1) for i in xrange(7)])
print index



left, width = .55, .5
bottom, height = .25, .5
right = left + width
top = bottom + height

bar_width = 4
#
opacity = 0.2
error_config = {'ecolor': '0.3'}
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size':9.5})
# rc('text', usetex=True)

f, (ax1) = plt.subplots(nrows=1, ncols=1)

# plt.ylabel("Time saved(%)", fontsize=11)
# ax1.set_title('Apache')
r1 = ax1.bar(index, get_data("NSGAII", "hv"), bar_width,alpha=opacity,color='#247BA0',error_kw=error_config, hatch="o")
r2 = ax1.bar(index+bar_width, get_data("SPEA2", "hv"), bar_width,alpha=opacity,color='#70C1B3',error_kw=error_config, hatch='*')
r3 = ax1.bar(index + 2*bar_width, get_data("GALE", "hv"), bar_width,alpha=opacity,color='#B2DBBF',error_kw=error_config, hatch='0')
r4 = ax1.bar(index + 3*bar_width, get_data("GALE_NM", "hv"), bar_width,alpha=opacity,color='#F3FFBD',error_kw=error_config, hatch='+')
r5 = ax1.bar(index + 4*bar_width, get_data("GALE_LP", "hv"), bar_width,alpha=opacity,color='#FF1654',error_kw=error_config, hatch='x')

# ax1.set_yscale('log', nonposy='clip')
# ax1.set_ylim(0, 119)
# ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.yaxis.offsetText.set_visible(False)

# ax1.set_ylabel("Mean(%) Fault Rate")
ax1.text(0.5, 0.95*(bottom+top), 'HyperVolume',
        horizontalalignment='center',
        verticalalignment='top',
        rotation=0,
        fontsize=15,
        transform=ax1.transAxes)
# ax1.set_yticks([0, 10, 20, 48],)
# ax1.set_yticklabels([0, 10, 20, 98.2])
# ax1.set_yscale('log', basey=10)
ax1.set_xticks([41, 71, 101, 131, 161, 191, 221])
ax1.set_xticklabels(["POM3A", "POM3B", "POM3C", "XOMO-OSP", "XOMO-OSP2", "XOMO-GROUND", "XOMO-FLIGHT"], fontsize=15)
ax1.tick_params(axis='y', labelsize=15)
ax1.set_xlim(22, 240)

# XOMO-FLIGHT,XOMO-GROUND, XOMO-OSP, XOMO-OSP2, POM3a, POM3b, POM3c


plt.figlegend([r1, r2, r3, r4, r5], ["NSGAII", "SPEA2", "GALE", "SWAY2", "SWAY5"], frameon=False, loc='upper center', bbox_to_anchor=(0.5, 1.013), fancybox=True, ncol=6, prop={'size':15})
# f.text(0.04, 0.5, 'Time Saved(%)', va='center', rotation='vertical', fontsize=11)
# plt.xlim(5, 125)
f.set_size_inches(14,7)
# f.subplots_adjust(wspace=0, hspace=0)
# plt.ylabel("Time saved(%)", fontsize=11)
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.tight_layout()
# plt.show()
plt.savefig('hypervolume.eps', format='eps')