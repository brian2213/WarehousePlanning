from Solver import *
from data_tool import *

class mainWareHouse(object):

    def __init__(self,LoadPickle=False, itemFile="", warehouseGridFile=""):
        self.model = warehouse_model(warehouseGridFile, itemFile=itemFile, LoadPickle=LoadPickle)
        self.solver=None

    def runSolver(self,countEffort=False, iter=1e2, orderlist=""):
        self.solver = Solver(self.model, orderlist=orderlist)
        self.solver.run('aStarSearch', countEffort=countEffort, iter=1e2)
        return self.solver.content


def mainTSPforUi(LoadPickle=False, countEffort=False, itemFile="", warehouseGridFile="", orderlist=""):
    warehouseGridFile = warehouseGridFile

    itemFile = itemFile
    orderlist = orderlist

    model = warehouse_model(warehouseGridFile, itemFile=itemFile, LoadPickle=LoadPickle)

    solver = Solver(model, orderlist=orderlist)

    solver.run('aStarSearch', countEffort=countEffort, iter=1e2)

    # solver.run('DynamicProgramming')

    return solver.content


if __name__ == "__main__":

    def mainTSP(LoadPickle=False, itemFile="", warehouseGridFile="", orderlist=""):
        if len(sys.argv) < 2:
            raise Exception('Must specify the warehouse file')

        warehouseGridFile = sys.argv[1]

        itemFile = sys.argv[2] if len(sys.argv) > 2 else ""

        orderlist = ""
        # orderlist = sys.argv[3] if len(sys.argv) > 3 else ""

        model = warehouse_model(warehouseGridFile, itemFile=itemFile, LoadPickle=LoadPickle, leftMode=True,
                                rightMode=False)

        solver = Solver(model, orderlist=orderlist)

        solver.run('aStarSearch', countEffort=False, iter=1e4, maxWeight=30)


    LoadPickle = False
    # cProfile.run('-s tottime mainTSP(LoadPickle)')
    mainTSP(LoadPickle)
    # BenchmarkShortestPath(LoadPickle)
