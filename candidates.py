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


class Candidate(object):
    def __init__(self, dec, obj, m, M):
        self.dec = dec
        self.obj = obj
        self.org_obj = [int(i) for i in self.obj]
        for x, (i,j) in enumerate(zip(m,M)):
            self.obj[x] = (self.obj[x]-i)/(j-i)

        self.wl = self.half_workload()

    def eval(self):
        return self.obj

    def half_workload(self):
        wl = 0
        for i in self.dec:
            if i <= 1: wl += 1
        return wl

    def __repr__(self):
        return str(self.dec) + '->' + str(self.obj)
