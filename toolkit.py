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
from math import sqrt, exp
import csv


def load_csv(folder, file_name, has_header=True):
    """
    loading the csv file at folder/file_name.csv
    :param folder:
    :param file_name:
    :param has_header:
    :return: (header if possible) + (content)
    """
    if not folder.endswith('/'):
        folder += '/'
    with open(folder + file_name+'.csv', 'r') as db:
        reader = csv.reader(db)
        if has_header:
            header = next(reader)
        content = []
        for line in reader:
            content.append(line)
    if has_header:
        return header, content
    else:
        return content


def str2num(s):
    try:
        s = int(s)
    except ValueError:
        try:
            s = float(s)
        except ValueError:
            pass
    return s


def _loss(f1, f2):
    return sum(exp(i - j) for i, j in zip(f1, f2)) / len(f1)


def cont_dominate(ind1, ind2):
    """
    Args:
        ind1:
        ind2:
    ALL VALUES ARE LESS IS MORE!!!!
    Returns: whether ind1 dominates ind2, i.e. True if ind1 is better than ind2
    """

    f1 = tuple(ind1.obj)
    f2 = tuple(ind2.obj)
    # f1 = _norm(f1)
    # f2 = _norm(f2)
    return _loss(f1, f2) < _loss(f2, f1)