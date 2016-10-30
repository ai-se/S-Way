from __future__ import division
from Problems.MONRP.monrp import MONRP
from jmoo_individual import *
import csv

from jmoo_algorithms import *

data_folder = "./Data/"


def func(problem, pop_size=100):
    filename = "Data/" + problem.name + "-p" + str(pop_size) + "-d" + str(len(problem.decisions)) + "-o" + \
                       str(len(problem.objectives)) + "-dataset.txt"

    population = []
    input = open(filename, 'rb')
    reader = csv.reader(input, delimiter=',')
    for k,p in enumerate(reader):
        if 0 < k <= pop_size:
            decisions = [float(p[n]) for n,dec in enumerate(problem.decisions)]
            objectives = problem.evaluate(decisions)
            population.append(jmoo_individual(problem,[float(p[n]) for n,dec in enumerate(problem.decisions)],objectives))
    assert(len(population) == pop_size), "something is wrong"

    # Format a population Data structure usable by DEAP's package
    dIndividuals = deap_format(problem, population)
    pareto_fronts = sortNondominated(dIndividuals, pop_size, first_front_only=True)

    assert(len(pareto_fronts) == 2), "Something is wrong"
    deap_nondominated_front = pareto_fronts[0]
    deap_dominated_front = pareto_fronts[-1]

    # Copy from DEAP structure to JMOO structure
    nondominated_front = []
    for i, dIndividual in enumerate(deap_nondominated_front):
        cells = []
        for j in range(len(dIndividual)):
            cells.append(dIndividual[j])
        nondominated_front.append(jmoo_individual(problem, cells, [f for f in dIndividual.fitness.values]))
    dominated_front = []
    for i, dIndividual in enumerate(deap_dominated_front):
        cells = []
        for j in range(len(dIndividual)):
            cells.append(dIndividual[j])
        dominated_front.append(jmoo_individual(problem, cells, [f for f in dIndividual.fitness.values]))
    assert(len(dominated_front) + len(nondominated_front) == pop_size), "something is wrong"

    pop_to_file(nondominated_front, "./RawData/Distance/" + problem.name + "_p-" + str(pop_size) + "_non_dominated.txt")
    pop_to_file(dominated_front, "./RawData/Distance/" + problem.name + "_p-" + str(pop_size) + "_dominated.txt")


def pop_to_file(population, filename):
    content = []
    for pop in population:
        decisions = pop.decisionValues
        objectives = pop.fitness.fitness
        content.append(decisions + objectives)
    import csv

    with open(filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(content)


if __name__ == "__main__":
    problems = [MONRP(50, 4, 5, 0, 90), MONRP(50, 4, 5, 0, 110), MONRP(50, 4, 5, 4, 90), MONRP(50, 4, 5, 4, 110)]
    for problem in problems:
        func(problem)