from Solver import *
from data_tool import *


# import cProfile

def mainTSP(LoadPickle=False,itemFile="",warehouseGridFile="",orderlist=""):
    if len(sys.argv) < 2:
        raise Exception('Must specify the warehouse file')

    warehouseGridFile = sys.argv[1]

    itemFile = sys.argv[2] if len(sys.argv) > 2 else ""

    orderlist=""
    # orderlist = sys.argv[3] if len(sys.argv) > 3 else ""


    model = warehouse_model(warehouseGridFile, itemFile=itemFile, LoadPickle=LoadPickle,leftMode=True,rightMode=True)

    solver = Solver(model, orderlist=orderlist)

    # solver.run('BranchAndBoundSearch',iter=1e4)

    # solver.run('aStarSearch', countEffort=True, iter=1e4)

    solver.run('aStarSearch', countEffort=True,iter=1e2)

    # solver.run('DynamicProgramming')

    # solver.run('tspPythonPermute')

    # solver.run('tspNonRecursion')

def mainTSPforUi(LoadPickle=False,countEffort=False,itemFile="",warehouseGridFile="",orderlist=""):

    warehouseGridFile = warehouseGridFile

    itemFile = itemFile
    # orderlist = sys.argv[3] if len(sys.argv) > 3 else ""
    orderlist=orderlist

    model = warehouse_model(warehouseGridFile, itemFile=itemFile, LoadPickle=LoadPickle)

    solver = Solver(model, orderlist=orderlist)

    # solver.run('BranchAndBoundSearch',iter=1e4)

    # solver.run('aStarSearch', countEffort=True, iter=1e4)

    solver.run('aStarSearch', countEffort=countEffort,iter=1e2)

    # solver.run('DynamicProgramming')

    # solver.run('tspPythonPermute')

    # solver.run('tspNonRecursion')

    return solver.content

if __name__ == "__main__":
    LoadPickle = False
    # cProfile.run('-s tottime mainTSP(LoadPickle)')
    mainTSP(LoadPickle)
    # BenchmarkShortestPath(LoadPickle)
