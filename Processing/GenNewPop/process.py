from __future__ import division
from random import choice
import os
import numpy as np

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

def buildHeader():
    "a header used with rrsl in jmoo_algorithms.py"

    header = ""
    for decision in xrange(decisions):
        header += "$" + str(decision) + ","
    for objective in xrange(objectives):
            header += ">>f" + str(objective) + ","

    return "".join(header[:len(header) - 1])  # remove the last comma at the end

def get_filename(foldername):
    """ Get a random file to generate the new population"""
    files = [data_folder + foldername + '/' + repetation + '/' for repetation in os.listdir(data_folder + foldername)]
    return choice(files)

def process(filename):
    objectives = []
    processed_filename = filename + "1.txt"
    content = ""

    # add header
    content += buildHeader() + "\n"

    # get content from filename
    raw_content = open(processed_filename).readlines()
    for line in raw_content:
        content += line

    # Extra valid solution that need to added
    extra_needed = 100 - len(raw_content)

    # Get the object of problem
    problem_name = "_".join(filename.split('/')[-3].split("_")[1:])
    problem_filenname = "ProblemData/" + "_".join(filename.split('/')[-3].split("_")[1:]) + '+10000.p'
    import pickle
    problem = pickle.load(open(problem_filenname, 'r'))

    f = open("./processed/" + problem_name + "-p100-d50-o3-dataset.txt", 'w')
    for _ in xrange(extra_needed):
        output_dec = problem.generateInput()
        output_obj = problem.evaluate(output_dec)
        objectives.append(output_obj)
        merged = ",".join(map(str, output_dec + output_obj))
        content += merged + '\n'

    objs = len(objectives[0])

    fitnessMedians = []
    fitnessLows = []
    fitnessUps = []


    for obj in xrange(objs):
        t_obj = [o[obj] for o in objectives]
        fitnessMedians.append(np.median(t_obj))
        fitnessLows.append(min(t_obj))
        fitnessUps.append(max(t_obj))

    print fitnessLows
    print fitnessMedians
    print fitnessUps
    print
    for i in xrange(len(fitnessLows)):
        print str(fitnessLows[i]) + "," + str(fitnessMedians[i]) + "," + str(fitnessUps[i])
        content += str(fitnessLows[i]) + "," + str(fitnessMedians[i]) + "," + str(fitnessUps[i]) + "\n"

    f.write(content)
    f.close()

if __name__ == "__main__":
    problems = os.listdir(data_folder)
    for problem in problems:
        selected_repetation = get_filename(problem)
        process(selected_repetation)