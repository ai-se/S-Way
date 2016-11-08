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


from __future__ import division
from candidates import Candidate
import toolkit
import pdb

def fetch_candidates(model):
    h, content = toolkit.load_csv('Init_pop', model, has_header=True)
    decNum = len([i for i in h if i.startswith('$')])
    objNum = len([i for i in h if i.startswith('>>')])

    contentT = map(list, zip(*content))
    DEC = contentT[:decNum]
    OBJ = contentT[decNum:]
    DEC = map(list, zip(*DEC))
    OBJ = map(list, zip(*OBJ))

    DEC = map(lambda l: map(lambda i:int(float(i)), l), DEC)
    OBJ = map(lambda l: map(lambda i:float(i), l), OBJ)

    # getting the min/max value for objectives
    objt = map(list, zip(*OBJ))
    m = [min(i) for i in objt]
    M = [max(i) for i in objt]

    candidates = list()
    for d,o in zip(DEC, OBJ):
        candidates.append(Candidate(d, o, m, M))

    return candidates

