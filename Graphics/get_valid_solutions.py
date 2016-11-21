from __future__ import division
import os
import pandas as pd
from random import choice
import numpy as np

data_folder = "./RawData/PopulationArchives/"

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


def find_extreme_points(points):
    from Techniques.euclidean_distance import euclidean_distance
    random_point = choice(points)
    distances = [euclidean_distance(point, random_point) for point in points]
    first_point = points[distances.index(max(distances))]
    distances = [euclidean_distance(point, first_point) for point in points]
    second_point = points[distances.index(max(distances))]
    return [first_point, second_point]


def find_files(problem, pop_size):
    folders = [data_folder + d + "/" for d in os.listdir(data_folder) if problem.name in d]
    folders_list = []
    for folder in folders:
        folders_list.extend([folder + f + "/" for f in os.listdir(folder) if ".DS_Store" not in f])
    file_list = []
    for folder in folders_list:
        file_list.extend([folder + f for f in os.listdir(folder) if ".DS_Store" not in f])
    content = []
    for files in file_list:
        df = pd.read_csv(files, header=None)
        y = df[df.columns[-1 * len(problem.objectives):]]
        temp_content = y.values.tolist()
        assert(len(temp_content) == len(df)), "something is wrong"
        content.extend(temp_content)

    return_list = []
    for obj_no in xrange(len(problem.objectives)):
        temp_list = [c[obj_no] for c in content]
        return_list.append([min(temp_list), max(temp_list)])

    normal_content = []
    for c in content:
        temp_content = []
        for obj in xrange(len(problem.objectives)):
            temp_content.append(100 * ((c[obj] - return_list[obj][0]) /
                    (return_list[obj][1] - return_list[obj][0])))
        normal_content.append(temp_content)

    extreme_points = find_extreme_points(normal_content)

    return return_list, extreme_points


def get_performance_measures(problem, pop_size):
    results = {}
    normalizing_values, extreme_points = find_files(problem, pop_size)
    folders = [data_folder + d + "/" for d in os.listdir(data_folder) if problem.name in d]
    folders_list = []
    for folder in folders:
        folders_list.extend([folder + f + "/" for f in os.listdir(folder) if ".DS_Store" not in f])

    # get only the last generation
    filtered_list = []
    for file in folders_list:
        if "SWAY5" in file:
            filtered_list.append(file + "1.txt")
        else:
            filtered_list.append(file + "20.txt")
    assert(len(folders_list) == len(filtered_list)), "Something is wrong"

    for filtered_file in filtered_list:
        df = pd.read_csv(filtered_file, header=None)
        full_content = df.values.tolist()
        decisions = [content[:-1 * len(problem.objectives)] for content in full_content]
        valid_solutions = []
        for decision_index, decision in enumerate(decisions):
            if problem.evalConstraints(decision) is True:
                valid_solutions.append(full_content[decision_index][-1 * len(problem.objectives):])

        content = valid_solutions
        if len(content) < 2:
            print ">"*10, filtered_file
            raw_input()
            break
        normalized_content = []
        assert(len(normalizing_values) == len(content[0])), "Something is wrong"
        for c in content:
            temp_content = []
            for obj in xrange(len(problem.objectives)):
                temp_content.append(100 * ((c[obj] - normalizing_values[obj][0])/
                                    (normalizing_values[obj][1] - normalizing_values[obj][0])))
            normalized_content.append(temp_content)
        assert(len(normalized_content) == len(content)), "Something is wrong"

        if "SC_" in filtered_file:
            algorithm_name = "-".join(filtered_file.split('/')[-3].split('_')[:2])
        else:
            algorithm_name = filtered_file.split('/')[-3].split('_')[0]

        population_size = filtered_file.split('/')[-3].split('_')[-1]
        repeat_no = filtered_file.split('/')[-2].split('.')[0]

        if algorithm_name+"_"+population_size not in results.keys():
            results[algorithm_name+"_"+population_size] = SolutionHolder(problem.name, algorithm_name)

        reference_point = [110 for _ in xrange(len(problem.objectives))]

        from PerformanceMetrics.HyperVolume.hv import get_hyper_volume
        hv = get_hyper_volume(reference_point, normalized_content)

        from PerformanceMetrics.Spread.Spread import spread_calculator
        spread = spread_calculator(normalized_content, extreme_points[0], extreme_points[-1])

        pfs = len(normalized_content)

        results[algorithm_name+"_"+population_size].add_score(hv, spread, pfs, None)

    transform_results = {}
    alg_name = {
        "NSGAIISC-1024": "NSGAIISC-1225",
        "NSGAIISC-2048": "NSGAIISC-2500",
        "NSGAIISC-4096": "NSGAIISC-5000",
        "NSGAIISC-10000": "NSGAIISC-10000",
        "SPEA2SC-1024": "SPEA2SC-1225",
        "SPEA2SC-2048": "SPEA2SC-2500",
        "SPEA2SC-4096": "SPEA2SC-5000",
        "SPEA2SC-10000": "SPEA2SC-10000",
    }
    for key in results.keys():
        algorithm_name = key.split("_")[0]
        population_size = key.split("_")[-1]
        problem_name = results[key].problem

        repeats = results[key].repeats
        hvs = [r.hv for r in repeats]
        spreads = [r.spread for r in repeats]
        pfs = [r.pfs for r in repeats]
        igds = [r.igd for r in repeats]

        print "Problem", ",",problem_name
        print "Algorithm",",", algorithm_name
        print "PopSize",",", population_size
        print "HV: ", hvs
        print "Spread: ", spreads
        print
        # print "Median-HV",",", np.median(hvs), ",",
        # print "IQR-HV", ",",np.percentile(hvs, 75) - np.percentile(hvs, 25), ",",
        # print "Median-spreads", ",",np.median(spreads), ",",
        # print "IQR-spreads", ",",np.percentile(spreads, 75) - np.percentile(spreads, 25), ",",
        # print "Median-PFS", ",",np.median(pfs), ",",
        # print "IQR-PFS", ",",np.percentile(pfs, 75) - np.percentile(pfs, 25)
        # print "Median-HV", np.median(hvs),
        # print "IQR-HV", np.percentile(hvs, 75) - np.percentile(hvs, 25),

        if problem_name not in transform_results.keys():
            transform_results[problem_name] = {}
            transform_results[problem_name]["HV"] = []
            transform_results[problem_name]["Spread"] = []

        if "SC" in algorithm_name:
            transform_results[problem_name]["HV"].append([alg_name[algorithm_name] + "_" + population_size] + hvs)
            transform_results[problem_name]["Spread"].append([alg_name[algorithm_name] + "_" + population_size] + spreads)
        else:
            transform_results[problem_name]["HV"].append([algorithm_name + "_" + population_size] + hvs)
            transform_results[problem_name]["Spread"].append([algorithm_name + "_" + population_size] + spreads)

    # write into pickle file
    import pickle
    pickle.dump(transform_results, open('./Results/' + problem.name + '.pickle', 'wb'))
