#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2016, Jianfeng Chen <jchen37@ncsu.edu>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

from data_pre import *
from subprocess import call
import toolkit
import csv
import pdb
import random

min_set = 100


def euclidean2(can1, can2):
    dest = 0
    for i, j in zip(can1.dec, can2.dec):
        dest += (i-j)**2
    return dest


def pune(group):
    random.shuffle(group)
    pivot = random.choice(group)
    tmp = list()
    for i in group:
        tmp.append((i, euclidean2(i, pivot)))
    sort_can = sorted(tmp, key=lambda x:x[1])
    east = sort_can[0][0]
    west = sort_can[-1][0]

    res = list()
    if toolkit.cont_dominate(east, west):
        for i in sort_can[:len(group)/2]:
            res.append(i[0])
    else:
        for i in sort_can[len(group)/2:]:
            res.append(i[0])

    random.shuffle(res)
    return res


def sway(candidates):
    if len(candidates) < min_set: return candidates

    cans = sorted(candidates, key=lambda i: i.wl)
    L = len(cans)
    g1, g2, g3, g4, g5 = cans[:L/5], cans[L/5: 2*L/5], cans[2*L/5: 3*L/5], cans[3*L/5: 4*L/5], cans[4*L/5:]

    remain = list()
    remain.extend(pune(g1))
    remain.extend(pune(g2))
    remain.extend(pune(g3))
    remain.extend(pune(g4))
    remain.extend(pune(g5))

    random.shuffle(remain)

    return sway(remain)

models = ['MONRP_50_4_5_0_110', 'MONRP_50_4_5_0_90', 'MONRP_50_4_5_4_110', 'MONRP_50_4_5_4_90']

for model in models:
    for repeat in range(20):
        call(['mkdir', 'RawData/PopulationArchives/'+'SWAY5_'+model+'/'+str(repeat)])
        # call(['rm', 'RawData/PopulationArchives/' + 'SWAY5_' + model + '/' + str(repeat)+'/0.csv'])
        candidates = fetch_candidates(model)
        sway_res = sway(candidates)

        with open('RawData/PopulationArchives/'+'SWAY5_'+model+'/'+str(repeat)+'/1.txt', 'w') as f:
            result_writer = csv.writer(f)
            for r in sway_res:
                result_writer.writerow(r.dec+r.org_obj)

        print('repeat %d for %s done.' % (repeat, model))
