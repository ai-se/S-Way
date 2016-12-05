from __future__ import division
from random import choice
import os

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)

sys.path.insert(0,grandparentdir)

from Problems.MONRP.monrp import MONRP

data_folder = "./PopulationArchives/"
decisions = 50
objectives = 3

object_holder = {
    "MONRP_50_4_5_0_110": MONRP(50, 4, 5, 0, 110),
    "MONRP_50_4_5_0_90": MONRP(50, 4, 5, 0, 90),
    "MONRP_50_4_5_4_110": MONRP(50, 4, 5, 4, 110),
    "MONRP_50_4_5_4_90": MONRP(50, 4, 5, 4, 90)

}

# def add_objectives(filename):


files = ["./data/" + f for f in os.listdir("./data/")]
for file in files:
    problem_name = file.split('/')[-1].split('-')[0]
    problem = object_holder[problem_name]
    content = open(file, 'r').readlines()

    f = open("./processed/" + problem_name + ".csv", 'w')
    f_content = ""
    for i,c in enumerate(content):
        if i==0:
            f_content += c
            continue
        dec = map(int, c.strip().split(', '))
        obj = problem.evaluate(dec)
        merged = ",".join(map(str, dec + obj))
        f_content += merged + '\n'

    f.write(f_content)
