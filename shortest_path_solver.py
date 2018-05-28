import sys
import time
from heapq import heappush, heappop


def shortestPathTime(model, node):
    warehouseGraph = model.warehouseGraph
    model = model.start
    end = model.end

    start_time = time.time();
    shortestPath(warehouseGraph, start, node)
    shortestPath(warehouseGraph, node, end)
    print("Time used for " + str(node) + " " + str(time.time() - start_time))


def shortestPath(warehouseGraph, startNode, targetNode):
    grid = warehouseGraph["items"]
    nodes = warehouseGraph["nodes"]
    edges = warehouseGraph["edges"]
    # print("")
    # # target=str(input("Search itemID:"))
    # if target not in grid:
    # 	print("warehouse has no such item")
    # 	return
    # targetpos=[grid[target][0],grid[target][1]]
    # targetNode=str(grid[target][0])+"*"+str(grid[target][1])+"*pick"
    # print("Target position:"+str(targetNode))
    # print("")
    # print("Searching:"+target)
    # pdb.set_trace()
    que = list()
    # startNode=str(start[0])+"*"+str(start[1])
    que.append([0, startNode, [startNode]])  # current cost,position, current routes

    minpath = sys.maxsize
    shortestpath = []
    visited = set()
    visited.add(startNode)
    while len(que) > 0:
        # point=que.pop(0)
        point = heappop(que)
        cost = point[0]
        # if the cost is greater than the current solution 
        # no need to run the loop
        if cost >= minpath:
            break

        curpos = point[1]
        routes = point[2]
        # print("routes:"+str(routes))
        if nodes.get(curpos) is None:
            continue
        reachableNodes = nodes[curpos]
        for dest in reachableNodes:
            if dest in visited:
                continue
            destpos = dest.split("*")
            # distanceTogoal=abs(targetpos[0]-int(destpos[0]))+abs(targetpos[1]-int(destpos[1]))
            distanceSofar = cost + edges[curpos + "-" + dest]
            # pdb.set_trace()
            newroutes = list(routes)
            newroutes.append(dest)
            newpoint = [distanceSofar, dest, newroutes]
            visited.add(dest)
            if dest == targetNode:
                if minpath >= distanceSofar:
                    # pdb.set_trace()
                    minpath = distanceSofar  ################ definition of cost should be change
                    shortestpath = newroutes
                else:
                    # shortestpath=newroutes
                    # pdb.set_trace()
                    break

            heappush(que, newpoint)

    # print("Shortest path:"+str(shortestpath))
    # print("Cost:"+str(minpath))
    return {"path": shortestpath, "cost": minpath}


def BenchmarkShortestPath(LoadPickle=False):
    h = hpy()

    warehouseData = readWarehouse(sys.argv[1])  # warehouseData contains {"items","minmax"}
    warehouseGraph = initWarehouse(warehouseData)  # warehouseGraph contains {"nodes","edges","items","minmax"}

    msize = h.heap().size
    start = "0*0"
    end = "0*0"

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

    shortestPathTime(warehouseGraph, start, end, '46071')
    shortestPathTime(warehouseGraph, start, end, '379019')
    shortestPathTime(warehouseGraph, start, end, '70172')
    shortestPathTime(warehouseGraph, start, end, '1321')
    shortestPathTime(warehouseGraph, start, end, '2620261')
