from __future__ import division
from sk import rdivDemo
import pickle
import numpy as np


def get_content(pickle_file):
    content = pickle.load(open(pickle_file, "rb"))
    problem_name = content.keys()[-1]
    # print problem_name
    for i in xrange(len(content[problem_name]['Spread'])):
        if content[problem_name]['Spread'][i][0] == 'SWAY5_10000':
            median_score = np.median(content[problem_name]['Spread'][i][1:])

    for ii in xrange(len(content[problem_name]['Spread'])):
        for j in xrange(1, len(content[problem_name]['Spread'][ii])):
            content[problem_name]['Spread'][ii][j] = (content[problem_name]['Spread'][ii][j] * 100) / median_score

    rdivDemo(content[problem_name]["Spread"], globalMinMax=False, isLatex=True)
    # raw_input()

if __name__ == "__main__":
    import os
    # files = [f for f in os.listdir(".") if ".pickle" in f]
    # import pdb; pdb.set_trace()
    # files
    # for f in files:
    #     get_content(f)
    models = ['POM3A', 'POM3B', 'POM3C', 'POM3D', 'xomo_all', 'xomo_flight', 'xomo_ground', 'xomo_osp', 'xomoo2']
    sizes = ['(S)', '(M)', '(L)', '']

    for m in models:
        print (m)
        for s in sizes:
            get_content('oct29/'+m+s+'.pickle')
        print ('~\par\n~\par\n')
        raw_input()
