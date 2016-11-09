from __future__ import division
from sk import rdivDemo
import pickle
import numpy as np

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
    problem_name = content.keys()[-1]
    for i in xrange(len(content[problem_name]['HV'])):
        if content[problem_name]['HV'][i][0] == 'SWAY5_100':
            median_score = np.median(content[problem_name]['HV'][i][1:])

    for ii in xrange(len(content[problem_name]['HV'])):
        for j in xrange(1, len(content[problem_name]['HV'][ii])):
            content[problem_name]['HV'][ii][j] = (content[problem_name]['HV'][ii][j] * 100) / median_score

    rdivDemo(content[problem_name]["HV"], globalMinMax=False, isLatex=False, lessismore=False)
    # raw_input()

def get_contentSPREAD(pickle_file):
    content = pickle.load(open(pickle_file, "rb"))
    problem_name = content.keys()[-1]
    for i in xrange(len(content[problem_name]['Spread'])):
        if content[problem_name]['Spread'][i][0] == 'SWAY5_100':
            median_score = np.median(content[problem_name]['Spread'][i][1:])

    for ii in xrange(len(content[problem_name]['Spread'])):
        for j in xrange(1, len(content[problem_name]['Spread'][ii])):
            content[problem_name]['Spread'][ii][j] = (content[problem_name]['Spread'][ii][j] * 100) / median_score

    rdivDemo(content[problem_name]["Spread"], globalMinMax=False, isLatex=False, lessismore=True)

if __name__ == "__main__":
    import os
    files = [f for f in os.listdir(".") if "MONRP" in f]
    for f in files:
        print f
        print "HyperVolume"
        get_contentHV(f)
        print "Spread"
        get_contentSPREAD(f)
        print "=" * 100