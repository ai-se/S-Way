from jmoo_objective import *
from jmoo_decision import *
from jmoo_problem import jmoo_problem
from Helper.pom3 import pom3


class POM3B(jmoo_problem):
    "POM3B"
    def __init__(prob, percentage=-1):
        prob.percentage=percentage
        prob.name = "POM3B"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency",
                 "Dynamism", "Size", "Plan", "Team Size"]
        LOWS = [0.10, 0.82, 80, 0.40, 0,   1, 0, 0, 1]
        UPS  = [0.90, 1.26, 95, 0.70, 100, 50, 2, 5, 20]
        prob.decisions = [jmoo_decision(names[i], LOWS[i], UPS[i]) for i in range(len(names))]
        prob.objectives = [jmoo_objective("Cost", True, None, None), jmoo_objective("Score", True, 0, 1),
                           # jmoo_objective("Completion", False, 0, 1)]
                          jmoo_objective("Idle", True, None, None)]

    def evaluate(prob, input = None):
        if input:
            for i,decision in enumerate(prob.decisions):
                decision.value = input[i]
        else: input = [decision.value for decision in prob.decisions]
        p3 = pom3()
        output = p3.simulate(input)
        for i,objective in enumerate(prob.objectives):
            objective.value = output[i]
        return [objective.value for objective in prob.objectives]

    def evalConstraints(prob,input = None):
        return False #no constraints


class POM3BS(jmoo_problem):
    "POM3B small (30% decision space of the original POM3B)"

    def __init__(prob, percentage=-1):
        prob.percentage=percentage
        prob.name = "POM3B(S)"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency",
                 "Dynamism", "Size", "Plan", "Team Size"]
        LOWS = [0.38, 0.974, 85.25, 0.505, 35.0, 18.15, 0.7, 1.75, 7.65]
        UPS  = [0.62, 1.106, 89.75, 0.595, 65.0, 32.85, 1.3, 3.25, 13.35]
        prob.decisions = [jmoo_decision(names[i], LOWS[i], UPS[i]) for i in range(len(names))]
        prob.objectives = [jmoo_objective("Cost", True, None, None), jmoo_objective("Score", True, 0, 1),
                           # jmoo_objective("Completion", False, 0, 1)]
                          jmoo_objective("Idle", True, None, None)]

    def evaluate(prob, input = None):
        if input:
            for i,decision in enumerate(prob.decisions):
                decision.value = input[i]
        else: input = [decision.value for decision in prob.decisions]
        p3 = pom3()
        output = p3.simulate(input)
        for i,objective in enumerate(prob.objectives):
            objective.value = output[i]
        return [objective.value for objective in prob.objectives]

    def evalConstraints(prob,input = None):
        return False #no constraints


class POM3BM(jmoo_problem):
    "POM3B medium (50% decision space of the original POM3B)"

    def __init__(prob, percentage=-1):
        prob.percentage=percentage
        prob.name = "POM3B(M)"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency",
                 "Dynamism", "Size", "Plan", "Team Size"]
        LOWS = [0.30, 0.93, 83.75, 0.475, 25.0, 13.25, 0.5, 1.25, 5.75]
        UPS  = [0.70, 1.15, 91.25, 0.625, 75.0, 37.75, 1.5, 3.75, 15.25]
        prob.decisions = [jmoo_decision(names[i], LOWS[i], UPS[i]) for i in range(len(names))]
        prob.objectives = [jmoo_objective("Cost", True, None, None), jmoo_objective("Score", True, 0, 1),
                           # jmoo_objective("Completion", False, 0, 1)]
                          jmoo_objective("Idle", True, None, None)]

    def evaluate(prob, input = None):
        if input:
            for i,decision in enumerate(prob.decisions):
                decision.value = input[i]
        else: input = [decision.value for decision in prob.decisions]
        p3 = pom3()
        output = p3.simulate(input)
        for i,objective in enumerate(prob.objectives):
            objective.value = output[i]
        return [objective.value for objective in prob.objectives]

    def evalConstraints(prob,input = None):
        return False #no constraints


class POM3BL(jmoo_problem):
    "POM3B large (70% decision space of the original POM3B)"

    def __init__(prob, percentage=-1):
        prob.percentage=percentage
        prob.name = "POM3B(L)"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency",
                 "Dynamism", "Size", "Plan", "Team Size"]
        LOWS = [0.22, 0.886, 82.25, 0.445, 15.0, 8.35, 0.3, 0.75, 3.85]
        UPS  = [0.78, 1.194, 92.75, 0.655, 85.0, 42.65, 1.7, 4.25, 17.15]
        prob.decisions = [jmoo_decision(names[i], LOWS[i], UPS[i]) for i in range(len(names))]
        prob.objectives = [jmoo_objective("Cost", True, None, None), jmoo_objective("Score", True, 0, 1),
                           # jmoo_objective("Completion", False, 0, 1)]
                          jmoo_objective("Idle", True, None, None)]

    def evaluate(prob, input = None):
        if input:
            for i,decision in enumerate(prob.decisions):
                decision.value = input[i]
        else: input = [decision.value for decision in prob.decisions]
        p3 = pom3()
        output = p3.simulate(input)
        for i,objective in enumerate(prob.objectives):
            objective.value = output[i]
        return [objective.value for objective in prob.objectives]

    def evalConstraints(prob,input = None):
        return False #no constraints