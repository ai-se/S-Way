import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

datas = [
    [9,1.287353982,"POM3A"],
    [9,1.188750912,"POM3B"],
    [9,1.227730413,"POM3C"],
    [9,1.752681613,"POM3D"],
    [27,0.637557057,"xomo_all"],
    [27,0.629329421,"xomo_flight"],
    [27,0.628227015,"xomo_ground"],
    [27,1.116775931,"xomo_osp"],
    [27,0.957310072,"xomoo2"]
]
datas = sorted(datas, key=lambda x:x[0])
plt.scatter([d[0] for d in datas], [d[1] for d in datas], marker='o', color='r', s=55)

for i, xy in enumerate(zip([d[0]+0.75 for d in datas], [d[1]*0.985 for d in datas])):
    ax.annotate('%s' % datas[i][-1], xy=xy, textcoords='data')
plt.xlabel("Actual Dimensions", fontsize=15)
plt.ylabel("Instrinsic Dimensions", fontsize=15)
# plt.xlim(0, 45)
# plt.ylim(0, 3.5)
plt.savefig("./underlying_dimension.eps")
