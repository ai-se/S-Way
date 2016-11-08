from __future__ import division
from sk import rdivDemo
import pickle
import numpy as np


def get_contentHV(pickle_file):

    content = pickle.load(open(pickle_file, "rb"))
    problem_name = content.keys()[-1]
    print problem_name
    for i in xrange(len(content[problem_name]['HV'])):
        if content[problem_name]['HV'][i][0] == 'SWAY5_10000':
            median_score = np.median(content[problem_name]['HV'][i][1:])

    for ii in xrange(len(content[problem_name]['HV'])):
        for j in xrange(1, len(content[problem_name]['HV'][ii])):
            content[problem_name]['HV'][ii][j] = (content[problem_name]['HV'][ii][j] * 100) / median_score

    rdivDemo(content[problem_name]["HV"], globalMinMax=False, isLatex=True)
    # raw_input()

def get_content(pickle_file):
    content = pickle.load(open(pickle_file, "rb"))
    problem_name = content.keys()[-1]
    print problem_name
    for i in xrange(len(content[problem_name]['Spread'])):
        if content[problem_name]['Spread'][i][0] == 'SWAY5_10000':
            median_score = np.median(content[problem_name]['Spread'][i][1:])

    for ii in xrange(len(content[problem_name]['Spread'])):
        for j in xrange(1, len(content[problem_name]['Spread'][ii])):
            content[problem_name]['Spread'][ii][j] = (content[problem_name]['Spread'][ii][j] * 100) / median_score

    rdivDemo(content[problem_name]["Spread"], globalMinMax=False, isLatex=False)
    raw_input()

if __name__ == "__main__":
    import os
    files = [f for f in os.listdir(".") if ".pickle" in f]
    for f in files:
        get_contentHV(f)