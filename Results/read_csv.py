from __future__ import division
import pickle
from sk import rdivDemo
import numpy as np

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0,parentdir)


class Scores:
    def __init__(self, hv, spread, pfs, igd):
        self.hv = hv
        self.spread = spread
        self.pfs = pfs
        self.igd = igd

class SolutionHolder:
    def __init__(self, problem, algorithm):
        self.problem = problem
        self.algorithm = algorithm
        self.repeats = []

    def add_score(self, hv, spread, pfs, igd):
        self.repeats.append(Scores(hv, spread, pfs, igd))


def get_contentHV(pickle_file):
    content = pickle.load(open(pickle_file, "rb"))
    print content[content.keys()[-1]].problem
    repeats = len(content[content.keys()[-1]].repeats)
    algorithms = content.keys()
    hvs = []
    for i in xrange(repeats):
        hvs.append(content['SWAY5_10000'].repeats[i].hv)
    median_score = np.median(hvs)

    passed = []
    for algorithm in algorithms:
        temp = [algorithm]
        for j in xrange(repeats):
            temp.append((content[algorithm].repeats[i].hv * 100) / median_score)
        passed.append(temp)
    rdivDemo(passed, globalMinMax=True, isLatex=True, lessismore=False)


def get_contentSPREAD(pickle_file):
    content = pickle.load(open(pickle_file, "rb"))
    repeats = len(content[content.keys()[-1]].repeats)
    algorithms = content.keys()
    spreads = []
    for i in xrange(repeats):
        spreads.append(content['SWAY5_10000'].repeats[i].spread)
    median_score = np.median(spreads)

    passed = []
    for algorithm in algorithms:
        temp = [algorithm]
        for j in xrange(repeats):
            temp.append((content[algorithm].repeats[i].spread * 100) / median_score)
        passed.append(temp)
    rdivDemo(passed, globalMinMax=True, isLatex=True, lessismore=False)

if __name__ == "__main__":
    import os
    files = [f for f in os.listdir(".") if "MONRP" in f]
    for f in files:
        # print f
        # print "HyperVolume"
        # get_contentHV(f)
        # print "Spread"
        get_contentSPREAD(f)
        # print "=" * 100
        # raw_input()