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
        # nsgaii_algorithms = [alg for alg in algorithms if "NSGA" in alg]
        # for alg in sorted(nsgaii_algorithms):
        #     print alg
        #     plt.plot(range(1, 21), container_dict[alg].hvs, label=alg)
        #     plt.plot(range(1, 21), container_dict[nsgaii_algorithms[0]].hvs, label=nsgaii_algorithms[0])
        #     plt.title(problem)
        #     plt.ylabel('HyperVolume')
        #     plt.legend(loc='lower center')
        #     plt.savefig("./Figures/NSGAII/" + problem + "_" + alg + "_Hypervolume", dpi=300)
        #     plt.cla()


        # # For SPEA2
        # spea2_algorithms = sorted([alg for alg in algorithms if "SPEA" in alg])
        # for alg in spea2_algorithms:
        #     print alg
        #     plt.plot(range(1, 21), container_dict[alg].hvs, label=alg)
        #     plt.plot(range(1, 21), container_dict[spea2_algorithms[0]].hvs, label=spea2_algorithms[0])
        #     plt.title(problem)
        #     plt.ylabel('HyperVolume')
        #     plt.legend(loc='lower center')
        #     plt.savefig("./Figures/SPEA2/" + problem + "_" + alg + "_Hypervolume", dpi=300)
        #     plt.cla()

        # For NSGA-II Spread
        nsgaii_algorithms = sorted([alg for alg in algorithms if "NSGA" in alg])
        for alg in (nsgaii_algorithms):
            print alg
            plt.plot(range(1, 21), container_dict[alg].spreads, label=alg)
            plt.plot(range(1, 21), container_dict[nsgaii_algorithms[0]].spreads, label=nsgaii_algorithms[0])
            plt.title(problem)
            plt.ylabel('Spread')
            plt.legend(loc='lower center')
            plt.savefig("./Figures/Spread_NSGAII/" + problem + "_" + alg + "_Spread", dpi=300)
            plt.cla()

        # For SPEA2 Spread
        # spea2_algorithms = sorted([alg for alg in algorithms if "SPEA" in alg])
        # for alg in spea2_algorithms:
        #     print alg
        #     plt.plot(range(1, 21), container_dict[alg].spreads, label=alg)
        #     plt.plot(range(1, 21), container_dict[spea2_algorithms[0]].spreads, label=spea2_algorithms[0])
        #     plt.title(problem)
        #     plt.ylabel('Spread')
        #     plt.legend(loc='lower center')
        #     plt.savefig("./Figures/Spread_SPEA2/" + problem + "_" + alg + "_Spread", dpi=300)
        #     plt.cla()

        # import pdb
        # pdb.set_trace()

if __name__ == "__main__":
    ingest_data("result.csv")