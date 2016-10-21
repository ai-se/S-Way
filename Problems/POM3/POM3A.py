from jmoo_objective import *
from jmoo_decision import *
from jmoo_problem import jmoo_problem
from Helper.pom3 import pom3


class POM3A(jmoo_problem):
    "POM3A"
    def __init__(prob, percentage=-1):
        prob.percentage=percentage
        prob.name = "POM3A"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
                 "Size", "Plan", "Team Size"]
        LOWS = [0.1, 0.82, 2, 0.40, 1, 1, 0, 0, 1]
        UPS = [0.9, 1.20, 10, 0.70, 100, 50, 4, 5, 44]
        prob.decisions = [jmoo_decision(names[i], LOWS[i], UPS[i]) for i in range(len(names))]
        # prob.objectives = [jmoo_objective("Cost", True, 0), jmoo_objective("Score", False, 0, 1),
        #                    jmoo_objective("Completion", False, 0, 1)]#, jmoo_objective("Idle", True, 0, 1)]
        prob.objectives = [jmoo_objective("Cost", True, 0), jmoo_objective("Score", True, 0, 1),
                           # jmoo_objective("Completion", False, 0, 1)]
                          jmoo_objective("Idle", True, 0, 1)]

    def evaluate(prob, input=None):
        if input:
            for i, decision in enumerate(prob.decisions):
                decision.value = input[i]
        else:
            input = [decision.value for decision in prob.decisions]
        p3 = pom3()
        output = p3.simulate(input)
        for i, objective in enumerate(prob.objectives):
            objective.value = output[i]
        return [objective.value for objective in prob.objectives]

    def evalConstraints(prob, input=None):
        return False  # no constraints


class POM3AS(POM3A):
    "POM3A Small (30% decision space of the original space)"
    def __init__(prob, percentage=-1):
        prob.percentage = percentage
        prob.name = "POM3A(S)"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
                 "Size", "Plan", "Team Size"]
        LOWS = [0.38, 0.953, 4.8, 0.505, 35.65, 18.15, 1.4, 1.75, 16]
        UPS = [0.62, 1.067, 7.2, 0.595, 65.35, 32.85, 2.6, 3.25, 28.95]
        prob.decisions = [jmoo_decision(names[i], LOWS[i], UPS[i]) for i in range(len(names))]
        # prob.objectives = [jmoo_objective("Cost", True, 0), jmoo_objective("Score", False, 0, 1),
        #                    jmoo_objective("Completion", False, 0, 1)]#, jmoo_objective("Idle", True, 0, 1)]
        prob.objectives = [jmoo_objective("Cost", True, 0), jmoo_objective("Score", True, 0, 1),
                           # jmoo_objective("Completion", False, 0, 1)]
                           jmoo_objective("Idle", True, 0, 1)]


class POM3AM(POM3A):
    "POM3A Medium (50% decision space of the original space)"
    def __init__(prob, percentage=-1):
        prob.percentage = percentage
        prob.name = "POM3A(M)"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
                 "Size", "Plan", "Team Size"]
        LOWS = [0.3, 0.915, 4.0, 0.475, 25.75, 13.25, 1.0, 1.25, 11.75]
        UPS = [0.7, 1.105, 8.0, 0.625, 75.25, 37.75, 3.0, 3.75, 33.25]
        prob.decisions = [jmoo_decision(names[i], LOWS[i], UPS[i]) for i in range(len(names))]
        # prob.objectives = [jmoo_objective("Cost", True, 0), jmoo_objective("Score", False, 0, 1),
        #                    jmoo_objective("Completion", False, 0, 1)]#, jmoo_objective("Idle", True, 0, 1)]
        prob.objectives = [jmoo_objective("Cost", True, 0), jmoo_objective("Score", True, 0, 1),
                           # jmoo_objective("Completion", False, 0, 1)]
                           jmoo_objective("Idle", True, 0, 1)]


class POM3AL(POM3A):
    "POM3A Large (70% decision space of the original space)"
    def __init__(prob, percentage=-1):
        prob.percentage = percentage
        prob.name = "POM3A(L)"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
                 "Size", "Plan", "Team Size"]
        LOWS = [0.22, 0.877, 3.2, 0.445, 15.85, 8.35, 0.6, 0.75, 7.45]
        UPS = [0.78, 1.143, 8.8, 0.655, 85.15, 42.65, 3.4, 4.25, 37.55]
        prob.decisions = [jmoo_decision(names[i], LOWS[i], UPS[i]) for i in range(len(names))]
        # prob.objectives = [jmoo_objective("Cost", True, 0), jmoo_objective("Score", False, 0, 1),
        #                    jmoo_objective("Completion", False, 0, 1)]#, jmoo_objective("Idle", True, 0, 1)]
        prob.objectives = [jmoo_objective("Cost", True, 0), jmoo_objective("Score", True, 0, 1),
                           # jmoo_objective("Completion", False, 0, 1)]
                           jmoo_objective("Idle", True, 0, 1)]
