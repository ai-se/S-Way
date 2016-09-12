from __future__ import division
import sys, os, inspect

parentdir = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "../")))
if parentdir not in sys.path:
    sys.path.insert(0, parentdir)

import pandas as pd
import numpy as np
from Techniques.euclidean_distance import euclidean_distance

distance_matrix = []


def get_c_r(content, r):
    global distance_matrix
    lines = len(content)
    sum_value = 0
    for i in xrange(lines):
        for j in xrange(i+1, lines):
            if distance_matrix[i][j] <= r:
                sum_value += 1
    print '#',
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


def run(cont):
    content = cont
    high_r = highest_r()
    values_r = [i*0.05*high_r for i in xrange(1, 20)]
    log_c_r = [get_c_r(content, r) for r in values_r]
    log_r = map(lambda x:np.log(x), values_r)
    slopes = []
    for i in xrange(len(log_r)-1):
        slopes.append((log_c_r[i+1]-log_c_r[i])/(log_r[i+1]-log_r[i]))
    return np.mean(slopes)


import os
files = [f for f in os.listdir("./data/")]
for file in files:
    print file,
    content = pd.read_csv("./data/" + file)
    indep = [c for c in content.columns if ">>" not in c]
    print len(indep),
    content = content[indep]
    generate_distance_matrix2(content)

    print run(content)