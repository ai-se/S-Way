from __future__ import division

class SolutionHolder:
    def __init__(self, problem, algorithm):
        self.problem = problem
        self.algorithm = algorithm
        self.hvs = []
        self.hvs_iqrs = []
        self.spreads = []
        self.spreads_iqrs = []

    def add_hv(self, hv):
        self.hvs.append(hv)

    def add_spread(self, spread):
        self.spreads.append(spread)

    def add_hv_iqr(self, hv_iqr):
        self.hvs_iqrs.append(hv_iqr)

    def add_spread_iqr(self, spread_iqr):
        self.spreads_iqrs.append(spread_iqr)


def get_area(y):
    from numpy import trapz
    # Compute the area using the composite trapezoidal rule.
    area = trapz(y, dx=100)
    return area


def ingest_data(filename):
    import pandas as pd
    content = pd.read_csv(filename)
    problems = content.Problem.unique().tolist()
    algorithms = content.Algorithm.unique().tolist()
    for problem in problems:
        container_dict = {}
        for gen in xrange(1, 21):
            for algorithm in algorithms:
                if algorithm not in container_dict.keys(): container_dict[algorithm] = SolutionHolder(problem, algorithm)
                filtered_gen = content[(content.GenNo == gen) & (content.Problem == problem) & (content.Algorithm == algorithm)]
                assert (len(filtered_gen) == 1), "Something is wrong"
                filtered_gen = filtered_gen.values.tolist()[0]
                container_dict[algorithm].add_hv(filtered_gen[4])
                container_dict[algorithm].add_spread(filtered_gen[6])
                container_dict[algorithm].add_hv_iqr(filtered_gen[5])
                container_dict[algorithm].add_spread_iqr(filtered_gen[7])

        # DRAWING
        import matplotlib.pyplot as plt

        # For NSGA-II
        nsgaii_algorithms = [' NSGAII-normal', ' NSGAIISC-100',' NSGAIISC-512', ' NSGAIISC-1024', ' NSGAIISC-2048', ' NSGAIISC-4096',  ' NSGAIISC-8192', ' NSGAIISC-10000', ]

        print problem,
        for alg in (nsgaii_algorithms):
            print round((get_area(container_dict[alg].hvs)/get_area(container_dict[nsgaii_algorithms[0]].hvs)) * 100, 3),
        print


        # # # For SPEA2
        # spea2_algorithms = [' SPEA2-normal', ' SPEA2SC-100', ' SPEA2SC-512', ' SPEA2SC-1024', ' SPEA2SC-2048', ' SPEA2SC-4096', ' SPEA2SC-8192', ' SPEA2SC-10000',]
        # print problem,
        # for alg in spea2_algorithms:
        #     print round((get_area(container_dict[alg].hvs)/get_area(container_dict[spea2_algorithms[0]].hvs)) * 100, 3),
        # print


        # For NSGA-II Spread
        # nsgaii_algorithms = [' NSGAII-normal', ' NSGAIISC-100',' NSGAIISC-512', ' NSGAIISC-1024', ' NSGAIISC-2048', ' NSGAIISC-4096',  ' NSGAIISC-8192', ' NSGAIISC-10000', ]
        #
        # print problem,
        # for alg in (nsgaii_algorithms):
        #     print round((get_area(container_dict[alg].spreads)/get_area(container_dict[nsgaii_algorithms[0]].spreads)) * 100, 3),
        # print


        # For SPEA2 Spread
        # spea2_algorithms = [' SPEA2-normal', ' SPEA2SC-100', ' SPEA2SC-512', ' SPEA2SC-1024', ' SPEA2SC-2048', ' SPEA2SC-4096', ' SPEA2SC-8192', ' SPEA2SC-10000',]
        # print problem,
        # print spea2_algorithms
        # for alg in spea2_algorithms:
        #     print round((get_area(container_dict[alg].spreads)/get_area(container_dict[spea2_algorithms[0]].spreads)) * 100, 3),
        # print

        # import pdb
        # pdb.set_trace()

if __name__ == "__main__":
    ingest_data("result.csv")
    # get_area()