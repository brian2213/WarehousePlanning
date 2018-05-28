import itertools
import sys
from heapq import heappush, heappop

# from guppy import hpy


def tspRecursion2(solver, orderNodes, num, visited=set(), nodeList=[], cost=0):
    pathMatrix = solver.model.pathMatrix
    warehouseGraph = solver.model.warehouseGraph
    start = solver.model.start
    end = solver.model.end
    if len(orderNodes) == num:
        # a=shortestPath(warehouseGraph,start,end)
        a = pathMatrix[start][end]
        return [cost + a["cost"], nodeList]
    minpath = []
    mincost = sys.maxsize
    for node in orderNodes:
        if node in visited:
            continue
        visited.add(node)
        # sho=shortestPath(warehouseGraph,start,node)
        sho = pathMatrix[start][node]

        nodeList.append(node)
        results = tspRecursion(pathMatrix, warehouseGraph, orderNodes, num + 1, node, end, visited, nodeList,
                               cost + sho["cost"])
        if mincost > results[0]:
            mincost = results[0]
            minpath = results[1]
        visited.remove(node)
        nodeList.pop()
    return [mincost, minpath]


def tspRecursion(solver, orderNodes, num, visited=set(), path=[], cost=0):
    pathMatrix = solver.model.pathMatrix
    warehouseGraph = solver.model.warehouseGraph
    start = solver.model.start
    end = solver.model.end
    if len(orderNodes) == num:
        # a=shortestPath(warehouseGraph,start,end)
        a = pathMatrix[start][end]
        # path+=(a["path"])
        # cost+=a["cost"]

        # minpath=list(path)
        # mincost=cost
        # print(minpath)
        # print(mincost)
        return [cost + a["cost"], path + (a["path"])]
    minpath = []
    mincost = sys.maxsize
    for node in orderNodes:
        if node in visited:
            continue
        visited.add(node)
        # sho=shortestPath(warehouseGraph,start,node)
        sho = pathMatrix[start][node]

        results = tspRecursion(pathMatrix, warehouseGraph, orderNodes, num + 1, node, end, visited,
                               path + (sho["path"][:-1]), cost + sho["cost"])
        if mincost > results[0]:
            mincost = results[0]
            minpath = results[1]
        visited.remove(node)
    return [mincost, minpath]


def tspNonRecursion(solver, orderNodes, iter=1e2, upperbound=sys.maxsize, printTree=False):
    pathMatrix = solver.model.pathMatrix
    warehouseGraph = solver.model.warehouseGraph
    start = solver.model.start
    end = solver.model.end

    que = [[0, [start]]]
    minpath = []
    mincost = sys.maxsize

    while len(que) > 0:
        cur = que.pop(0)
        visited = set(cur[1])
        cost = cur[0]
        for node in orderNodes:
            if node in visited:
                continue
            newCost = cost + pathMatrix[cur[1][-1]][node]["cost"]
            que.append([newCost, cur[1] + [node]])
            if len(cur[1]) == len(orderNodes) and mincost > newCost:
                mincost = newCost
                minpath = cur[1] + [node]
    minpath.append(end)
    start = solver.start
    shortestpath = minpath
    fullpath = []
    for i in range(1, len(shortestpath)):
        fullpath += pathMatrix[start][shortestpath[i]]["path"][:-1]
        start = shortestpath[i]
    fullpath.append(start)

    return [mincost, fullpath]


def tspPythonPermute(solver, orderNodes, iter=1e2, upperbound=sys.maxsize, printTree=False):
    pathMatrix = solver.model.pathMatrix
    warehouseGraph = solver.model.warehouseGraph
    start = solver.model.start
    end = solver.model.end

    orders = itertools.permutations(orderNodes, len(orderNodes))
    mincost = sys.maxsize
    minpath = []
    for order in orders:
        cost = 0
        start = solver.start
        for node in list(order):
            if node == start:
                continue
            cost += pathMatrix[start][node]["cost"]
            start = node
        cost += pathMatrix[start][end]["cost"]
        if mincost > cost:
            mincost = cost
            minpath = order

    start = solver.start
    shortestpath = minpath
    fullpath = []
    for i in range(0, len(shortestpath)):
        fullpath += pathMatrix[start][shortestpath[i]]["path"][:-1]
        start = shortestpath[i]
    fullpath += pathMatrix[start][end]["path"]

    return [mincost, fullpath]


def DynamicProgramming(solver, orderNodes, iter=1e2, upperbound=sys.maxsize, printTree=False):
    pathMatrix = solver.model.pathMatrix
    warehouseGraph = solver.model.warehouseGraph
    start = solver.model.start
    end = solver.model.end
    # h=hpy()
    # msize=h.heap().size

    orderNodes = list(orderNodes)
    orderNodes.insert(0, start)
    # orderNodes.append(end)
    # print(orderNodes)
    n = len(orderNodes)
    C = {}
    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (pathMatrix[orderNodes[0]][orderNodes[k]]["cost"], 0)

    for sub_size in range(2, n):
        for sub in itertools.combinations(range(1, n), sub_size):
            # Set bits for all nodes in this sub
            bits = 0
            for bit in sub:
                bits |= 1 << bit

            # Find the lowest cost to get to this sub
            for k in sub:
                prev = bits & ~(1 << k)

                res = []
                for m in sub:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + pathMatrix[orderNodes[m]][orderNodes[k]]["cost"], m))
                C[(bits, k)] = min(res)
    # We're interested in all bits but the least significant (the start state)
    bits = (2 ** n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + pathMatrix[orderNodes[k]][end]["cost"], k))
    opt, parent = min(res)
    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    # Add implicit start state
    path.append(0)
    # return opt, list(reversed(path))

    path = [orderNodes[x] for x in list(reversed(path))]
    path.append(end)

    fullpath = []
    for i in range(1, len(path)):
        fullpath += pathMatrix[start][path[i]]["path"][:-1]
        start = path[i]
    fullpath.append(end)
    # printer("Used memory for TSP,"+str((h.heap().size-msize)/float(1024*1024)))
    return [opt, fullpath]


def UniformCostSearch(solver, orderNodes, upperbound=sys.maxsize):
    pathMatrix = solver.model.pathMatrix
    start = solver.model.start
    end = solver.model.end

    orderNodes = list(orderNodes)
    # orderNodes.insert(0,start)
    visited = set()
    que = []
    que.append([0, [start], visited])
    # visited.add(start)
    shortestpath = []
    cnt = 1e5
    while len(que) > 0 and cnt > 0:
        cnt -= 1
        route = que.pop(0)
        route = heappop(que)
        preNode = route[1][-1]
        cost = route[0]
        if cost > upperbound:
            break
        visited = route[2]
        for node in orderNodes:
            if node in visited:
                continue
            newcost = cost + pathMatrix[preNode][node]['cost']
            newRoute = route[1] + [node]
            visited.add(node)
            if len(orderNodes) + 1 == len(newRoute):
                newcost = newcost + pathMatrix[node][end]['cost']
                if upperbound > newcost:
                    upperbound = newcost
                    shortestpath = newRoute + [end]
                    continue
            heappush(que, [newcost, newRoute, set(visited)])
            visited.remove(node)

        while len(que) > 0 and que[-1][0] > upperbound:
            que.pop()

    return [upperbound, shortestpath]


def BranchAndBoundSearch(solver, orderNodes, iter=1e2, upperbound=sys.maxsize, printTree=False):
    pathMatrix = solver.model.pathMatrix
    start = solver.model.start
    end = solver.model.end

    # h = hpy()
    # msize = h.heap().sizex

    def deepCopyMatrix(costMatix):
        copiedMatrix = []
        for i in range(len(costMatix)):
            copiedMatrix.append([])
            for j in range(len(costMatix)):

                copiedMatrix[i].append(costMatix[i][j])

        return copiedMatrix

    def reduceMatrice(costMatix):

        reducedMatrx = deepCopyMatrix(costMatix)
        # reduce row
        cost = 0
        for i in range(len(costMatix)):
            minVal = sys.maxsize
            for j in range(len(costMatix)):
                if costMatix[i][j] != sys.maxsize:
                    if costMatix[i][j] < minVal:
                        minVal = costMatix[i][j]
            if minVal == sys.maxsize:
                continue
            cost += minVal

            for j in range(len(costMatix)):
                if costMatix[i][j] != sys.maxsize:
                    reducedMatrx[i][j] -= minVal

        # reduce col
        for i in range(len(costMatix)):
            minVal = sys.maxsize
            for j in range(len(costMatix)):
                if reducedMatrx[j][i] != sys.maxsize:
                    if reducedMatrx[j][i] < minVal:
                        minVal = reducedMatrx[j][i]

            if minVal == sys.maxsize:
                continue
            cost += minVal

            for j in range(len(costMatix)):
                if costMatix[j][i] != sys.maxsize:
                    reducedMatrx[j][i] -= minVal

        return [cost, reducedMatrx]

    def invalidateMatrice(costMatix, start, end):
        # invalid path

        reducedMatrx = deepCopyMatrix(costMatix)
        cost = 0
        if reducedMatrx[start][end] != sys.maxsize:
            cost = reducedMatrx[start][end]
        else:
            cost = 0
        for i in range(len(costMatix)):
            reducedMatrx[start][i] = sys.maxsize
            reducedMatrx[i][end] = sys.maxsize
        reducedMatrx[start][end] = sys.maxsize
        reducedMatrx[end][start] = sys.maxsize
        return [cost, reducedMatrx]

    orderNodes = list(orderNodes)
    orderNodes.insert(0, start)
    orderNodes.append(end)

    # extract cost matrix by order
    costMatix = []
    for i in range(len(orderNodes)):
        costMatix.append([])
        for j in range(len(orderNodes)):
            if orderNodes[i] != orderNodes[j]:
                costMatix[i].append(pathMatrix[orderNodes[i]][orderNodes[j]]['cost'])
            else:
                costMatix[i].append(sys.maxsize)

    # set all node to start point to infinity and end to all node to infinity
    for i in range(len(orderNodes)):
        costMatix[len(orderNodes) - 1][i] = sys.maxsize
        costMatix[i][0] = sys.maxsize
    # for sub in costMatix:
    # 	printer(sub)
    cost, costMatix = reduceMatrice(costMatix)

    visited = set()
    que = []
    que.append([cost, [0], visited, costMatix, 0])
    visited.add(0)
    shortestpath = []
    cnt = iter
    upperbound = sys.maxsize

    edges = []
    nodeid = 0
    while len(que) > 0 and cnt > 0:
        cnt -= 1
        route = heappop(que)
        cost = route[0]

        if cost >= upperbound:
            continue
        preNode = route[1][-1]
        visited = route[2]
        costMatix = route[3]
        prenodeid = route[4]  # for print search tree

        for i in range(1, len(orderNodes) - 1):
            if i in visited or preNode == i:
                continue

            newcost, newMatrix = invalidateMatrice(costMatix, preNode, i)

            newcost += cost
            newRoute = route[1] + [i]

            if len(orderNodes) - 1 == len(newRoute):
                newcost = newcost + newMatrix[i][len(orderNodes) - 1]

                if upperbound > newcost:
                    upperbound = newcost
                    shortestpath = newRoute + [len(orderNodes) - 1]

                # for sub in newMatrix:
                # 	printer(sub)

                continue

            reducedcost, newMatrix = reduceMatrice(newMatrix)

            visited.add(i)
            nodeid += 1
            if printTree:
                edges += [(prenodeid, nodeid)]
            heappush(que, [newcost + reducedcost + len(orderNodes) - len(newRoute), newRoute, set(visited), newMatrix,
                           nodeid])
            visited.remove(i)
    cost = 0
    fullpath = []
    for i in range(1, len(shortestpath)):
        cost += pathMatrix[start][orderNodes[shortestpath[i]]]['cost']
        fullpath += pathMatrix[start][orderNodes[shortestpath[i]]]["path"][:-1]
        start = orderNodes[shortestpath[i]]
    fullpath.append(end)
    # cost+=pathMatrix[start][end]['cost']

    if printTree:
        pickle.dump((nodeid, edges), open("edges.p", "wb"))
    # printer("Used memory for A*,"+str((h.heap().size-msize)/float(1024*1024)))
    # printer("node expended,"+str(nodeid+1))
    return [cost, fullpath]


def aStarSearch(solver, orderNodes, upperbound=sys.maxsize, iter=1e2, printTree=False):
    pathMatrix = solver.model.pathMatrix
    start = solver.model.start
    end = solver.model.end

    # h=hpy()
    # msize=h.heap().size

    orderNodes = list(orderNodes)
    # orderNodes.insert(0,start)
    visited = set()
    que = []

    Totalcost = 0
    weightSofar = 1

    TotalWeight = 0
    if solver.countEffort:
        for node in solver.itemlist:
            TotalWeight += solver.model.itemProperty[node].weight if node in solver.model.itemProperty else \
            solver.model.itemProperty['avg']

    # prediction for the root node is not necessary
    #
    # for node in orderNodes:
    #     Totalcost += pathMatrix[node][end]['cost']
    # Totalcost += pathMatrix[start][end]['cost']

    que.append([Totalcost, 0, [start], visited, 0, weightSofar])
    # visited.add(start)
    shortestpath = []
    nodeid = 0
    edges = []

    while len(que) > 0 and iter > 0:
        iter -= 1
        # route=que.pop(0)
        route = heappop(que)
        cost = route[1]
        if cost >= upperbound:
            continue
        # break  #early termination

        preNode = route[2][-1]
        visited = route[3]
        prenodeid = route[4]  # for print search tree
        Totalcost = 0
        weightSofar = route[5]
        # TotalWeight = 0
        for node2 in orderNodes:  # predict the cost until finish
            if node2 not in visited:
                Totalcost += pathMatrix[node2][end]['cost']

        for node in orderNodes:
            if node in visited:
                continue
            newcost = cost + pathMatrix[preNode][node]['cost'] * weightSofar
            newRoute = route[2] + [node]
            # visited.add(node)
            if len(orderNodes) + 1 == len(newRoute):
                newcost = newcost + pathMatrix[node][end]['cost'] * weightSofar
                if upperbound > newcost:
                    upperbound = newcost
                    shortestpath = newRoute + [end]

                continue

            visited.add(node)
            nodeid += 1
            if printTree:
                edges += [(prenodeid, nodeid)]

            weight = 0
            if solver.countEffort:

                for item in solver.containerMap[node]:
                    weight += solver.model.itemProperty[item].weight if item in solver.model.itemProperty else \
                        solver.model.itemProperty['avg']

                heuristic=TotalWeight - weightSofar
            else:
                heuristic=1

            heappush(que,
                     [Totalcost * (heuristic) + newcost, newcost, newRoute, set(visited), nodeid,
                      weightSofar + weight])
            visited.remove(node)

    # while len(que)>0 and que[-1][1]>upperbound:
    # 	que.pop()
    fullpath = []
    for i in range(1, len(shortestpath)):
        fullpath += pathMatrix[start][shortestpath[i]]["path"][:-1]
        start = shortestpath[i]
    fullpath.append(end)
    if printTree:
        pickle.dump((nodeid, edges), open("edges.p", "wb"))
    # printer("Used memory for A*,"+str((h.heap().size-msize)/float(1024*1024)))
    # printer("node expended,"+str(nodeid+1))

    return [upperbound, fullpath]


def BenchmarkTSP(model, LoadPickle=False):
    h = hpy()

    warehouseData = readWarehouse(sys.argv[1])  # warehouseData contains {"items","minmax"}
    warehouseGraph = initWarehouse(warehouseData)  # warehouseGraph contains {"nodes","edges","items","minmax"}

    msize = h.heap().size
    start = "0*0"
    end = "18*0"

    # create path matrix
    # LoadPickle=True
    if LoadPickle:
        pathMatrix = pickle.load(open("save.p", "rb"))
        pathMatrix = pathMapMiniComplete(warehouseGraph, pathMatrix, start, end)
    else:
        # pathMatrix=pathMap(warehouseGraph)

        pathMatrix = pathMapMini(warehouseGraph)
        pathMatrix = pathMapMiniComplete(warehouseGraph, pathMatrix, start, end)
        pickle.dump(pathMatrix, open("save.p", "wb"))

    orders = readOrder(sys.argv[2])
