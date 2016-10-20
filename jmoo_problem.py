
"""
##########################################################
### @Author Joe Krall      ###############################
### @copyright see below   ###############################

    This file is part of JMOO,
    Copyright Joe Krall, 2014.

    JMOO is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    JMOO is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with JMOO.  If not, see <http://www.gnu.org/licenses/>.
    
###                        ###############################
##########################################################
"""

"Brief notes"
"Representation of a Multi-Objective Problem."

from jmoo_individual import *
import random,csv
class jmoo_problem(object):
    "a representation of a multi-objective problem"
    
    def __init__(prob):
        "jmoo problems are implemented via subclasses in jmoo_problems.py"
        prob.name = ""
        prob.decisions = []
        prob.objectives = []
        prob.numEvals = 0
        prob.percentage=0

    def generateInput(prob, center=False):
        "a way to generate decisions for this problem"
        while True: # repeat if we don't meet constraints
            temp_value = []
            if center is True:
                for decision in prob.decisions:
                    temp_value.append(random.uniform(decision.low + (decision.up - decision.low)*0.2, decision.up - (decision.up - decision.low)*0.2 ))
            else:
                for decision in prob.decisions:
                    temp_value.append(random.uniform(decision.low, decision.up))
            # if not prob.evalConstraints():
            #     break
            if prob.validate(temp_value) is True: break
        assert(prob.validate(temp_value) is True), "Something's wrong"
        # print "Initial Population Generation Complete"
        return temp_value

    def generateExtreme(prob):
        
        for decision in prob.decisions:
            decision.value = decision.low
            
        if prob.evalConstraints(): return prob.generateInput()
        return [decision.value for decision in prob.decisions]

    def loadInitialPopulation(problem, MU, repeat, path=""):
        "a way to load *the* initial problem as used in jmoo_jmoea.py"
        "this will load a csv as generated by the dataGen method of"
        "jmoo_problems.py"
        population_size = 100
        if path == "":
            filename = "./RawData/PopulationArchives/SWAY5_" + problem.name + "_" + str(population_size) \
                   + "/" + str(repeat) + "/" + "1.txt"

        elif path == "unittesting":
            filename = "../../Data/Testing-dataset.txt"
        else:
            print "No accounted for"
            exit()

        print "Filename: ", filename
        input = open(filename, 'rb')
        reader = csv.reader(input, delimiter=',')
        population = []
        
        #Use the csv file to build the initial population
        for k,p in enumerate(reader):
            print k, MU
            if k > MU:
                problem.objectives[k-MU-1].med = 100
                lownotfound = False
                upnotfound = False

                if problem.objectives[k-MU-1].low == None:
                    problem.objectives[k-MU-1].low = 100
                    lownotfound = True
                if problem.objectives[k-MU-1].up == None:
                    problem.objectives[k-MU-1].up = 100
                    upnotfound = True
            elif k > 0:
                population.append(jmoo_individual(problem,[float(p[n]) for n,dec in enumerate(problem.decisions)],None))
                #population[-1].fitness = jmoo_fitness(problem, [float(p[n+len(problem.decisions)]) for n,obj in enumerate(problem.objectives)])

        for k in xrange(len(problem.objectives)):
            problem.objectives[k].med = 100
            lownotfound = False
            upnotfound = False
            if problem.objectives[k].low == None:
                problem.objectives[k].low = 100
                lownotfound = True
            if problem.objectives[k].up == None:
                problem.objectives[k].up = 100
                upnotfound = True

        # generate Extra solutions:
        remaining = MU - len(population)
        for i in range(remaining):
            population.append(jmoo_individual(problem, problem.generateInput(), None))
        return population
    
    def buildHeader(prob):
        "a header used with rrsl in jmoo_algorithms.py"
        
        header = ""
        for decision in prob.decisions:
            header += "$" + decision.name + ","
        for objective in prob.objectives:
            if objective.lismore:
                header += ">>" + objective.name + ","
            else:
                header += "<<" + objective.name + ","          
        return header[:len(header)-1]  # remove the last comma at the end

    def validate(prob, decision_value):
        assert(len(decision_value) == len(prob.decisions)), "Something is wrong with the usage of validate function"
        for i, decision in enumerate(prob.decisions):
            if decision.low <= decision_value[i] <= decision.up: pass
            else:
                print  decision.low , decision_value[i] , decision.up
                return False
        return True


