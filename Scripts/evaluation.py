data = {}
data["ground"] = {}
data["ground"]["GALE"]={"evals":175.4}
data["ground"]["NSGAII"]={"evals":2000}
data["ground"]["SPEA2"]={"evals":2000}
data["ground"]["GALE_NM"]={"evals":14}
data["ground"]["GALE_LP"]={"evals":73.7}

data["POM3A"] = {}
data["POM3A"]["GALE"]={"evals":179.3}
data["POM3A"]["NSGAII"]={"evals":2000}
data["POM3A"]["SPEA2"]={"evals":2000}
data["POM3A"]["GALE_NM"]={"evals":14}
data["POM3A"]["GALE_LP"]={"evals":60}


data["POM3B"] = {}
data["POM3B"]["GALE"]={"evals":175}
data["POM3B"]["NSGAII"]={"evals":2000}
data["POM3B"]["SPEA2"]={"evals":2000}
data["POM3B"]["GALE_NM"]={"evals":14}
data["POM3B"]["GALE_LP"]={"evals":70}


data["POM3C"] = {}
data["POM3C"]["GALE"]={"evals":175}
data["POM3C"]["NSGAII"]={"evals":2000}
data["POM3C"]["SPEA2"]={"evals":2000}
data["POM3C"]["GALE_NM"]={"evals":14}
data["POM3C"]["GALE_LP"]={"evals":75}


data["XOMO_OSP"] = {}
data["XOMO_OSP"]["GALE"]={"evals":175.9}
data["XOMO_OSP"]["NSGAII"]={"evals":2000}
data["XOMO_OSP"]["SPEA2"]={"evals":2000}
data["XOMO_OSP"]["GALE_NM"]={"evals":14}
data["XOMO_OSP"]["GALE_LP"]={"evals":74}


data["XOMOO2"] = {}
data["XOMOO2"]["GALE"]={"evals":175.9}
data["XOMOO2"]["NSGAII"]={"evals":2000}
data["XOMOO2"]["SPEA2"]={"evals":2000}
data["XOMOO2"]["GALE_NM"]={"evals":14}
data["XOMOO2"]["GALE_LP"]={"evals":65}


data["XOMO_Flight"] = {}
data["XOMO_Flight"]["GALE"]={"evals":169.6}
data["XOMO_Flight"]["NSGAII"]={"evals":2000}
data["XOMO_Flight"]["SPEA2"]={"evals":2000}
data["XOMO_Flight"]["GALE_NM"]={"evals":14}
data["XOMO_Flight"]["GALE_LP"]={"evals":77}

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
r1 = ax1.bar(index, get_data("NSGAII", "evals"), bar_width,alpha=opacity,color='#247BA0',error_kw=error_config, hatch="o")
r2 = ax1.bar(index+bar_width, get_data("SPEA2", "evals"), bar_width,alpha=opacity,color='#70C1B3',error_kw=error_config, hatch='*')
r3 = ax1.bar(index + 2*bar_width, get_data("GALE", "evals"), bar_width,alpha=opacity,color='#B2DBBF',error_kw=error_config, hatch='0')
r4 = ax1.bar(index + 3*bar_width, get_data("GALE_NM", "evals"), bar_width,alpha=opacity,color='#F3FFBD',error_kw=error_config, hatch='+')
r5 = ax1.bar(index + 4*bar_width, get_data("GALE_LP", "evals"), bar_width,alpha=opacity,color='#FF1654',error_kw=error_config, hatch='x')
# r6 = ax1.bar(index + 5*bar_width, get_data("GALE_LPI", "evals"), bar_width,alpha=opacity,color='#00D9FA',error_kw=error_config)
ax1.set_yscale('log', nonposy='clip')
# ax1.set_ylim(0, 119)
# ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.yaxis.offsetText.set_visible(False)

# ax1.set_ylabel("Mean(%) Fault Rate")
ax1.text(0.5, 0.95*(bottom+top), 'Evaluations',
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
plt.savefig('evaluation.eps', format='eps')