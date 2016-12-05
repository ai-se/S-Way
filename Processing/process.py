from __future__ import division
from random import choice
import os

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

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
    problem = object_holder[problem_name]
    for _ in xrange(extra_needed):
        output_dec = problem.generateInput()
        output_obj = problem.evaluate(output_dec)
        import pdb
        pdb.set_trace()


    import pdb
    pdb.set_trace()

if __name__ == "__main__":
    problems = os.listdir(data_folder)
    for problem in problems:
        selected_repetation = get_filename(problem)
        process(selected_repetation)