import sys
import time

import matplotlib.pyplot as plt

import TSP_solver


class Solver(object):

    def __init__(self, model, **kwargs):

        self.model = model
        self.orderlist = kwargs.pop('orderlist', [])
        self.iter = kwargs.pop('iter', 1e3)
        self.content = ""
        self.orderNodes = []
        self.itemlist = []
        self.countEffort = False
        self.containerMap = {}  # give a node show all items in this node
        self.maxWeight = sys.maxsize

        self.leftMode = True
        self.rightMode = False
        self.CombineOrder = False
        self.WeightLimit = False

        self.routePoints = []
        self.originRoutePoints = []

        self.combinedOrder = []
        self.splitedOrder = []

    def run(self, tsp_solver='aStarSearch', countEffort=False, iter=1e4, maxWeight=sys.maxsize, leftMode=True,
            rightMode=False, orders="", WeightLimit=False, CombineOrder=False, orderlist=""):

        self.leftMode = leftMode
        self.rightMode = rightMode

        self.tsp_solver = tsp_solver
        self.countEffort = countEffort
        self.iter = iter
        self.maxWeight = maxWeight
        self.WeightLimit = WeightLimit
        self.CombineOrder = CombineOrder
        self.orderlist = orderlist

        if not hasattr(TSP_solver, self.tsp_solver):
            raise ValueError('Invalid update_rule "%s"' % self.tsp_solver)
        self.tsp_solver = getattr(TSP_solver, self.tsp_solver)

        if len(self.orderlist) > 0:
            self.runWithCSV(self.orderlist)
        else:
            self.runWithUserSpecified(orders)

    def printer(self, s):
        self.content += str(s) + "\n"
        print(s)

    def writeOutFile(self, content):
        f = open("optimized.csv", "w+")
        f.write(self.content)
        f.close()

    def originalDistance(self, orderlist):
        pathMatrix = self.model.pathMatrix
        warehouseData = self.model.warehouseData
        start = self.model.start
        end = self.model.end

        self.printer("Start Location," + str(start))
        self.printer("End Location," + str(end))

        items = warehouseData["items"]
        locs = [str(items[x][0]) + "*" + str(items[x][1]) + "*pick" for x in orderlist]
        locs.insert(0, start)
        locs.append(end)
        # print("Original Order,"+','.join(locs))
        cost = 0
        path = []
        totalWeight = 1
        for order in orderlist:
            if self.leftMode:
                node = str(items[order][0]) + "*" + str(items[order][1]) + "*pick"
            else:
                node = str(items[order][0] + 1) + "*" + str(items[order][1]) + "*pick"
            # print(node)
            # print(pathMatrix[start][node])
            if node == start:
                continue

            if self.countEffort:
                if order in self.model.itemProperty:
                    weight = self.model.itemProperty[order].weight
                else:
                    weight = self.model.itemProperty['avg']
            else:
                weight = 0

            cost += pathMatrix[start][node]["cost"] * totalWeight
            path += pathMatrix[start][node]["path"][:-1]
            start = node
            totalWeight += weight
            pass
        cost += pathMatrix[start][end]["cost"] * totalWeight
        path += pathMatrix[start][end]["path"]
        global originalPath
        originalPath = path
        self.printer("Original path," + ','.join(path))
        self.printer("Original cost," + str(cost))

    def runWithCSV(self, orderFile):

        orders = self.model.readOrder(orderFile)

        self.content = ""

        orders = self.orderCombiner(orders)

        self.printer("Planning routes from " + str(orderFile))
        start_time = time.time()
        num = 1  # for draw image
        contents = [self.content]
        for orderlist in orders:
            if len(orderlist) == 0:
                continue
            self.itemlist = orderlist
            self.content = ""
            self.printer("Order NO. ," + str(num) + "\n")
            num += 1
            contents.append(self.planner(orderlist))

        self.printer("Total Time for order," + str(time.time() - start_time))
        contents.append(self.content)
        self.content = "".join(contents)
        self.writeOutFile(self.content)

    def runWithUserSpecified(self, order=""):
        self.content = ""

        def pathToPoints(minpath):
            points = []
            for node in minpath:
                val = node.split('*')
                x = 0
                y = 0
                if len(val) > 2:
                    y += 0.5
                x += float(val[0])
                y += float(val[1])
                points.append([x, y])
            return points

        print("Planning from user specified list")
        self.itemlist = []

        # self.itemlist=self.model.setOrderLists(self.model.warehouseData)
        # self.itemlist = "281610	342706	111873	198029	366109	287261	76283	254489	258540	286457".split()
        self.itemlist = order.split()
        self.itemlist = self.weightSplit(self.itemlist)

        self.originRoutePoints = []
        self.routePoints = []
        for smalllist in self.itemlist:

            if len(smalllist) == 0:
                print("No Items are specified")
            else:
                self.content += (self.planner(smalllist))
            global originalPath
            points = pathToPoints(originalPath)

            self.originRoutePoints.append(points)
            # plt.figure(0)
            # self.plotTour(points)
            #
            # global minpath
            self.routePoints.append(pathToPoints(minpath))
            # plt.figure(1)
            # self.plotTour(points)
            #
            # plt.show()

        self.writeOutFile(self.content)

    def planner(self, nodelist):

        self.model.nodelist = nodelist
        # self.content = ""
        if len(nodelist) == 0:
            return ""

        self.printer("Items," + ','.join(nodelist))
        start_time = time.time()

        self.optimizeNodeToVisited(nodelist)
        self.printer("Distinct places," + ','.join(self.orderNodes))
        self.originalDistance(nodelist)
        lowerBound = self.MSTLowerBound(self.orderNodes)
        self.printer("LowerBound," + str(lowerBound))

        results = self.tsp_solver(self, self.orderNodes, iter=self.iter)

        # minpath.append(end)
        self.printer("Shortest Path," + ','.join(list(results[1])))
        self.printer("Shortest Path Cost," + str(results[0]))

        elapsed_time = time.time() - start_time

        self.printer("Computation Time," + str(elapsed_time) + "\n\n")

        global minpath
        minpath = results[1]
        return self.content

    def orderCombiner(self, orderlist):
        '''combine order to the same trip'''

        if self.maxWeight == sys.maxsize or not self.CombineOrder:
            return orderlist

        lists = []
        newlist = []
        weight = 0

        for order in orderlist:
            for item in order:
                itemW = self.getItemWeight(item)
                weight += itemW
                if weight > self.maxWeight:
                    weight = itemW
                    lists.append(newlist)
                    newlist = []
                newlist.append(item)
        lists.append(newlist)

        self.combinedOrder = lists
        return lists

    def weightSplit(self, orderlist):
        '''split the order if the list contains items weigh too much'''
        if self.maxWeight == sys.maxsize or not self.WeightLimit:
            return [orderlist]
        lists = []
        newlist = []
        weight = 0

        for item in orderlist:
            itemW = self.getItemWeight(item)
            weight += itemW
            if weight > self.maxWeight:
                weight = itemW
                lists.append(newlist)
                newlist = []
            newlist.append(item)

        lists.append(newlist)
        self.splitedOrder = lists
        return lists

    def getItemWeight(self, item):
        if item in self.model.itemProperty:
            itemW = float(self.model.itemProperty[item].weight)
        else:
            print(item + " weight is unknown, set to average")
            itemW = float(self.model.itemProperty['avg'])
        return itemW

    def optimizeNodeToVisited(self, nodelist):
        self.orderNodes = set()
        self.containerMap = {}

        edges = {}
        nodes = {}
        bothSide = self.leftMode == True and self.rightMode == True

        for order in nodelist:
            positions = self.itemIDtoNode(order)

            if bothSide:
                edge = str(positions[0]) + "-" + str(positions[1])
                if edge not in edges:
                    edges[edge] = positions

            for position in positions:
                if position not in self.containerMap:
                    self.containerMap[position] = []
                self.containerMap[position].append(order)
                self.orderNodes.add(position)
                if bothSide:
                    if position not in nodes:
                        nodes[position] = set()
                    nodes[position].add(edge)

        # if only one side available no need to reduce
        nodesNeedToVisited = []
        if bothSide:
            # both side available

            # potential solution :sepcial case vertex cover
            # pickUP place as node, item as edge
            # to find minimum nodes to get all item

            for node, incidents in nodes.items():
                # pick up nodes with two edges first
                # then delete edges
                if len(incidents) == 2:
                    nodesNeedToVisited.append(node)
                    for incident in incidents:
                        if incident in edges:
                            edges.pop(incident)
            # add rest node
            for edge, node in edges.items():
                nodesNeedToVisited.append(node[0])

            self.orderNodes = nodesNeedToVisited

    def MSTLowerBound(self, orderNodes):
        '''Calculating the lower bound for TSP'''

        pathMatrix = self.model.pathMatrix
        start = self.model.start
        end = self.model.end

        # Implementing Kruskal algorithm
        edges = []
        nodes = list(orderNodes)
        nodes.append(start)

        unionId = [x for x in range(len(nodes))]  # Quick Union find implementation

        def root(idx):
            while idx != unionId[idx]:
                idx = unionId[idx]
            return idx

        # nodes=set([orderNodes,start]) # consider duplicate the end node will be compute later
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i != j:
                    edges.append([pathMatrix[nodes[i]][nodes[j]]['cost'], i, j])

        edges.sort(key=lambda edge: edge[0])

        cost = 0
        visited = set()

        for edge in edges:
            iid = root(edge[1])
            jid = root(edge[2])
            if iid != jid:  # simple Union find implementation
                cost += edge[0]
                visited.add(edge[1])
                visited.add(edge[2])
                if len(visited) == len(nodes):
                    break

                unionId[iid] = jid  # union
        # pdb.set_trace()
        lowerBound = sys.maxsize
        for node in nodes:
            if node != end:
                endcost = pathMatrix[node][end]['cost']
                lowerBound = (cost + endcost) if lowerBound > (cost + endcost) else lowerBound

        return lowerBound

    def itemIDtoNode(self, target):
        # print("")
        warehouseData = self.model.warehouseData
        grid = warehouseData["items"]
        # target=str(input("Search itemID:"))
        if target not in grid:
            print("warehouse has no such item")
            return
        targetpos = [grid[target][0], grid[target][1]]
        targetNode = []
        if self.leftMode:
            targetNode.append(str(grid[target][0]) + "*" + str(grid[target][1]) + "*pick")
        if self.rightMode:
            targetNode.append(str(grid[target][0] + 1) + "*" + str(grid[target][1]) + "*pick")
        # print("Target position:"+str(targetNode))
        # print("")
        # print("Searching:"+target)
        return targetNode

    def plotTour(self, points):
        minmax = self.model.minmax
        plt.axis(minmax)
        plt.xticks(range(minmax[0], minmax[1], 1))
        plt.yticks(range(minmax[2], minmax[3], 1))
        for i in range(1, len(points), 1):
            x1 = [points[i - 1][0], points[i][0]]
            y1 = [points[i - 1][1], points[i][1]]
            plt.plot(x1, y1, marker='o')
        plt.grid(True)
        # plt.show()

        # content+=s
