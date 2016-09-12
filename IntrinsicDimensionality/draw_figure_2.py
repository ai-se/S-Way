import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

datas = [
    [9,1.287353982,"POM3A \n(9)"],
    [9,1.188750912,"POM3B \n(9)"],
    [9,1.227730413,"POM3C \n(9)"],
    [9,1.752681613,"POM3D \n(9)"],
    [27,0.637557057,"xomo\nall \n(27)"],
    [27,0.629329421,"xomo\nflight \n(27)"],
    [27,0.628227015,"xomo\nground \n(27)"],
    [27,1.116775931,"xomo\nosp \n(27)"],
    [27,0.957310072,"xomoo2\n (27)"]
]
datas = sorted(datas, key=lambda x:x[1])


x = [2*i for i in xrange(1, len(datas)+1)]
y = [d[1] for d in datas]

my_xticks = [d[-1] for d in datas]
plt.xticks(x, my_xticks, fontsize=11)
plt.yticks(fontsize=12)

plt.scatter(x, y, marker='o', color='r', s=55)
# plt.xlabel("Actual Dimensions", fontsize=15)
plt.ylabel("Instrinsic Dimensions")
# plt.xlim(0, 45)
# plt.ylim(0, 3.5)
plt.savefig("./underlying_dimension_2.eps")
