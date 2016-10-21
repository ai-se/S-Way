from jmoo_objective import *
from jmoo_decision import *
from jmoo_problem import jmoo_problem
from Helper.pom3 import pom3


class POM3D(jmoo_problem):
    "POM3D"

    def __init__(prob, percentage=-1):
        prob.percentage=percentage
        prob.name = "POM3D"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
                 "Size", "Plan", "Team Size"]
        LOWS = [0.10, 0.82, 2, 0.60, 80, 1, 0, 0, 10]
        UPS = [0.20, 1.26, 8, 0.95, 100, 10, 2, 5, 20]
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


class POM3DS(jmoo_problem):
    "POM3D 30% * decision space"

    def __init__(prob, percentage=-1):
        prob.percentage=percentage
        prob.name = "POM3D(S)"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
                 "Size", "Plan", "Team Size"]
        LOWS = [0.135, 0.974, 4.1, 0.7225, 87.0, 4.15, 0.7, 1.75, 13.5]
        UPS = [0.136, 0.9784, 4.16, 0.726, 87.2, 4.24, 0.72, 1.8, 13.6]
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


class POM3DM(jmoo_problem):
    "POM3D * 50% decision space"

    def __init__(prob, percentage=-1):
        prob.percentage=percentage
        prob.name = "POM3D(M)"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
                 "Size", "Plan", "Team Size"]
        LOWS = [0.125, 0.93, 3.5, 0.6875, 85.0, 3.25, 0.5, 1.25, 12.5]
        UPS = [0.175, 1.15, 6.5, 0.8625, 95.0, 7.75, 1.5, 3.75, 17.5]
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


class POM3DL(jmoo_problem):
    "POM3D * 70% decision space"

    def __init__(prob, percentage=-1):
        prob.percentage=percentage
        prob.name = "POM3D(L)"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
                 "Size", "Plan", "Team Size"]
        LOWS = [0.115, 0.886, 2.9, 0.6525, 83.0, 2.35, 0.3, 0.75, 11.5]
        UPS = [0.185, 1.194, 7.1, 0.8975, 97.0, 8.65, 1.7, 4.25, 18.5]
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