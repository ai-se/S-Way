from __future__ import division
import sys, os, inspect, math

import pandas as pd
import numpy as np

distance_matrix = []

def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance


def get_c_r(content, r):
    global distance_matrix
    lines = len(content)
    sum_value = 0
    for i in xrange(lines):
        for j in xrange(i+1, lines):
            if distance_matrix[i][j] <= r:
                sum_value += 1
    # print '#',
    sys.stdout.flush()
    c_r = (2/(lines * (lines-1))) * sum_value
    return np.log(c_r)


def highest_r():
    global distance_matrix
    max_value = -1e20
    for d in distance_matrix:
            max_value = max(max_value, max(d))
    return max_value

def generate_distance_matrix(content):
    lines = len(content)
    global distance_matrix
    for i in xrange(lines):
        temp = []
        for j in xrange(lines):
            temp.append(euclidean_distance(content.iloc[i], content.iloc[j]))
        distance_matrix.append(temp)

def generate_distance_matrix2(X):
    global distance_matrix
    from scipy.spatial.distance import pdist, squareform
    distance_matrix = squareform(pdist(X,'euclidean'))

def check_numeric(number_arrary, i):
    if math.isinf(number_arrary[i]) is False and math.isinf(number_arrary[i+1]) is False:
        return True
    return False


def run(cont):
    global distance_matrix
    content = cont
    number_of_dimensions = len(content.columns)
    max_dist = distance_matrix.max()
    values_r = [max_dist*i*0.02 for i in xrange(1, 51)]
    log_c_r = [get_c_r(content, r) for r in values_r]
    log_r = map(lambda x:np.log(x), values_r)
    slopes = []
    for i in xrange(len(log_r)-1):
        if check_numeric(log_c_r, i) is True:
            slopes.append((log_c_r[i+1]-log_c_r[i])/(log_r[i+1]-log_r[i]))
    
    return np.median(slopes)


def run_discreate(cont):
    global distance_matrix
    content = cont
    number_of_dimensions = len(content.columns)
    max_dist = distance_matrix.max()
    values_r = [i**0.5 for i in xrange(1, number_of_dimensions * (5-2))]
    log_c_r = [get_c_r(content, r) for r in values_r]
    log_r = map(lambda x:np.log(x), values_r)
    slopes = []
    for i in xrange(len(log_r)-1):
        if check_numeric(log_c_r, i) is True:
            slopes.append((log_c_r[i+1]-log_c_r[i])/(log_r[i+1]-log_r[i]))
            
    return np.median(slopes)

def draw():
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)

    datasPOM = [[9, 1.0086778334610971, 'POM3A'], [9, 0.8960354698836932, 'POM3B'], [9, 0.8428302403257556, 'POM3C'], [9, 1.2017948475021516, 'POM3D']]
    datasXOMO = [[27, 0.64100083134723196, 'xomo_all'], [27, 0.70135028665794363, 'xomo_flight'], [27, 0.62408143079524703, 'xomo_ground'], [27, 0.66892006443856389, 'xomo_osp'], [27, 0.63695912276029265, 'xomoo2']]
    datasMONRP = [[50, 17.471415619730941, 'MONRP_50_4_5_0_110'], [50, 21.218951390802751, 'MONRP_50_4_5_0_90'], [50, 21.177288918846827, 'MONRP_50_4_5_4_110'], [50, 21.701917154819849, 'MONRP_50_4_5_4_90']]

    plt.scatter([d[0] for d in datasPOM], [d[1] for d in datasPOM], marker='o', color='b', label='POM')
    plt.scatter([d[0] for d in datasXOMO], [d[1] for d in datasXOMO], marker='x', color='g', label='XOMO')
    plt.scatter([d[0] for d in datasMONRP], [d[1] for d in datasMONRP], marker='v', color='r', label='MONRP')

    ax.set_yscale('log')
    ax.legend(frameon=False, loc='lower center', bbox_to_anchor=(0.48, -0.225), fancybox=True, ncol=3)
    plt.xlabel("Actual Dimensions", fontsize=15)
    plt.ylabel("Instrinsic Dimensions", fontsize=15)
    plt.xlim(0, )
    plt.ylim(0, 30)
    plt.savefig("./underlying_dimension.eps", bbox_inches='tight', format='eps')

# results = []

# files = [f for f in os.listdir("./Data") if ".txt" in f and "MONRP" not in f]
# for file in files:
#     print file,
#     content = pd.read_csv("./Data/" + file)
#     indep = [c for c in content.columns if ">>" not in c]
#     print len(indep),
#     content = content[indep].head(100)
#     generate_distance_matrix2(content)
#     under_dim = run(content)
#     results.append([len(indep), under_dim, file.split('-')[0]])

# files = [f for f in os.listdir("./Data") if ".txt" in f and "MONRP" in f]
# for file in files:
#     print file,
#     content = pd.read_csv("./Data/" + file)
#     indep = [c for c in content.columns if ">>" not in c]
#     print len(indep),
#     content = content[indep].head(100)
#     generate_distance_matrix2(content)
#     under_dim = run_discreate(content)
#     results.append([len(indep), under_dim, file.split('-')[0]])

draw()
