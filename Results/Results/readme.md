Data: October 19, 2016

This folder contains all the pickle files after processing. 
Each pickle would have a dictionary with key
Algorithm.name + "_" + Population_Size

Each element would be of Type SolutionHolder

```
class SolutionHolder:
    def __init__(self, problem, algorithm):
        self.problem = problem
        self.algorithm = algorithm
        self.repeats = []
```

and repeats would have list of element of type Scores 

```
class Scores:
    def __init__(self, hv, spread, pfs, igd):
        self.hv = hv
        self.spread = spread
        self.pfs = pfs
        self.igd = igd
```