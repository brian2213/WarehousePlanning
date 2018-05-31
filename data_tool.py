import pickle

from shortest_path_solver import *


class warehouse_model():
    def __init__(self, warehouseFile, itemFile="", LoadPickle=False,leftMode=True,rightMode=True):
        start_time = time.time();
        self.minmax = [0, 0, 0, 0]  # represent minx,maxx,miny,maxy
        self.leftMode=leftMode
        self.rightMode=rightMode

        self.warehouseData = self.readWarehouse(warehouseFile)  # warehouseData contains {"items","minmax"}
        self.warehouseGraph = self.initWarehouse(
            self.warehouseData)  # warehouseGraph contains {"nodes","edges","items","minmax"}
        self.itemProperty = self.readItemProperty(itemFile)
        print("Time spent on initialize warehouse data:" + str(time.time() - start_time))
        # print("Memory used on initialize warehouse data:"+str((h.heap().size-msize)/float(1024*1024)))
        # self.content = ""


        # msize=h.heap().size
        # start=setStartPos(warehouseData)
        # end=setEndPos(warehouseData)

        self.start = "0*0"
        self.end = "18*0"
        start_time = time.time()
        # create path matrix
        # LoadPickle=True
        if LoadPickle:
            self.pathMatrix = pickle.load(open("save.p", "rb"))
            self.pathMatrix = self.pathMapMiniComplete(self)
        else:
            # pathMatrix=pathMap(warehouseGraph)

            self.pathMatrix = self.pathMapMini(self.warehouseGraph)
            self.pathMatrix = self.pathMapMiniComplete(self)
            pickle.dump(self.pathMatrix, open("save.p", "wb"))

        print("Time spent on preprosssing path cost:" + str(time.time() - start_time))

    # print("Memory used on preprosssing path cost:"+str((h.heap().size-msize)/float(1024*1024)))

    # decide the running mode

    def readWarehouse(self, warehouse):
        grid = dict()
        minmax = self.minmax
        gridLength = 10
        print("")
        print("Read warehouse")
        print("Reading " + str(warehouse) + " File..")
        print("")
        with open(warehouse, 'r') as f1:
            for line in f1:
                elements = line.split(',')
                grid[elements[0]] = [int(elements[1].split('.')[0]), int(elements[2].split('.')[0])]
                minmax[0] = grid[elements[0]][0] if grid[elements[0]][0] < minmax[0] else minmax[0]
                minmax[1] = grid[elements[0]][0] if grid[elements[0]][0] > minmax[1] else minmax[1]
                minmax[2] = grid[elements[0]][1] if grid[elements[0]][1] < minmax[2] else minmax[2]
                minmax[3] = grid[elements[0]][1] if grid[elements[0]][1] > minmax[3] else minmax[3]
        print("Warehouse dimension")
        print("min x : " + str(minmax[0]))
        print("max x : " + str(minmax[1]))
        print("min y : " + str(minmax[2]))
        print("max y : " + str(minmax[3]))
        print("")
        return {"items": grid, "minmax": minmax}

    def readOrder(self, Ordersfile):
        print("")
        print("Read Orders")
        print("Reading " + str(Ordersfile) + " File..")
        print("")

        with open(Ordersfile, 'r') as f1:
            orders = []
            # i=0
            for line in f1:
                elements = line.split()
                orders.append(elements)
            # i+=1
            return orders

    class item(object):
        def __init__(self, id, length=1, width=1, height=1, weight=1):
            self.id = id
            self.length = length
            self.width = width
            self.height = height
            self.weight = weight

    def readItemProperty(self, file):
        if file =="":
            return{}
        itemProperty = {}
        sum=0
        with open(file, 'r') as f1:
            f1.readline()  # skip first line for label
            # Item id length (inches) width (inches)	 height (inches) weight (lbs)
            for line in f1:
                id, length, width, height, weight = line.split()
                itemProperty[id] = self.item(id, float(length), float(width),float(height), float(weight))
                # print(line)
                sum+=float(weight)

        itemProperty['avg']=sum/len(itemProperty)
        print(itemProperty['avg'])
        return itemProperty

    def initWarehouse(self, warehouseData, gridLength=10):
        '''Intialize the warehouseModel by tha data with default gridLength = 10'''

        nodes = dict()
        edges = dict()
        
        minmax = warehouseData["minmax"]
        grid = warehouseData["items"]
        print("Initializing warehouse graph...")
        # Adding egde
        for y in range(minmax[2], minmax[3] + 2):
            for x in range(minmax[0], minmax[1] + 2):
                if nodes.get(str(x) + "*" + str(y)) == None:
                    nodes[str(x) + "*" + str(y)] = []
                nodes[str(x) + "*" + str(y)].append(str(x + 1) + "*" + str(y))
                edges[str(x) + "*" + str(y) + "-" + str(x + 1) + "*" + str(
                    y)] = gridLength  # edge length between two nodes
                nodes[str(x) + "*" + str(y)].append(str(x) + "*" + str(y + 1))
                edges[str(x) + "*" + str(y) + "-" + str(x) + "*" + str(y + 1)] = gridLength
        # Adding reverse edge

        for y in range(minmax[2], minmax[3] + 2)[::-1]:
            for x in range(minmax[0], minmax[1] + 2)[::-1]:
                if nodes.get(str(x) + "*" + str(y)) == None:
                    nodes[str(x) + "*" + str(y)] = []
                nodes[str(x) + "*" + str(y)].append(str(x - 1) + "*" + str(y))
                edges[str(x) + "*" + str(y) + "-" + str(x - 1) + "*" + str(y)] = gridLength
                nodes[str(x) + "*" + str(y)].append(str(x) + "*" + str(y - 1))
                edges[str(x) + "*" + str(y) + "-" + str(x) + "*" + str(y - 1)] = gridLength

        print("Update items into warehouse graph")
        # Injecting item to warehouse
        for key, pos in grid.items():

            if self.leftMode:
                # left bottom node
                itemPosLB = str(pos[0]) + "*" + str(pos[1])

                #### exact item node at left side
                itemPosLPick = itemPosLB + "*pick"

                # left top node
                itemPosLT = str(pos[0]) + "*" + str(pos[1] + 1)

                if nodes.get(itemPosLPick) == None:

                    nodes[itemPosLPick]=[itemPosLB,itemPosLT]
                    nodes[itemPosLB].append(itemPosLPick)
                    edges[itemPosLB + "-" + itemPosLPick] = gridLength / 2
                    edges[itemPosLPick + "-" + itemPosLB] = gridLength / 2
                    nodes[itemPosLT].append(itemPosLPick)
                    edges[itemPosLT + "-" + itemPosLPick] = gridLength / 2
                    edges[itemPosLPick + "-" + itemPosLT] = gridLength / 2

            if self.rightMode:
                # right bottom node
                itemPosRB = str(pos[0] + 1) + "*" + str(pos[1])

                #### exact item node at right side
                itemPosRPick = itemPosRB + "*pick"

                # right top node
                itemPosRT = str(pos[0] + 1) + "*" + str(pos[1] + 1)

                if nodes.get(itemPosRPick) == None:
                    nodes[itemPosRPick] = [itemPosRB, itemPosRT]
                    nodes[itemPosRB].append(itemPosRPick)
                    edges[itemPosRB + "-" + itemPosRPick] = gridLength / 2
                    edges[itemPosRPick + "-" + itemPosRB] = gridLength / 2
                    nodes[itemPosRT].append(itemPosRPick)
                    edges[itemPosRT + "-" + itemPosRPick] = gridLength / 2
                    edges[itemPosRPick + "-" + itemPosRT] = gridLength / 2

        print("")
        return {"nodes": nodes, "edges": edges, "minmax": minmax, "items": grid}

    def setPos(self, warehouseData):
        minmax = warehouseData["minmax"]
        sx = 0
        sy = 0

        print("Setting up the position")
        while True:
            sx = input("Input X point (integer):")
            try:
                val = int(sx)
                if int(sx) > minmax[1] or int(sx) < minmax[0]:
                    print("x value out of warehouse range")
                    continue
                break
            except ValueError:
                print("x value is not number")
        while True:
            sy = input("Input Y point (integer):")
            try:
                val = int(sy)
                if val > minmax[3] or val < minmax[2]:
                    print("y value out of warehouse range")
                    continue
                break
            except ValueError:
                print("x value is not number")
        start = [int(sx), int(sy)]
        print("")
        return str(start[0]) + "*" + str(start[1])

    def setStartPos(self, warehouseData):
        print("Set up start point")
        return self.setPos(warehouseData)

    def setEndPos(self, warehouseData):
        print("Set up end point")
        return self.setPos(warehouseData)

    def pathMap(self, warehouseGraph):
        print("pre-computing path matrix\n")
        nodes = warehouseGraph["nodes"]
        path = dict()

        for start in nodes:
            path[start] = dict()
            for end in nodes:
                if start != end:
                    path[start][end] = shortestPath(warehouseGraph, start, end)
        return path

    def pathMapMini(self, warehouseGraph):
        print("pre-computing path matrix\n")
        nodes = warehouseGraph["nodes"]
        path = dict()
        for begin in nodes:
            if "pick" not in begin:
                continue
            path[begin] = dict()
            for stop in nodes:
                if "pick" not in stop:
                    continue
                if begin != stop:
                    path[begin][stop] = shortestPath(warehouseGraph, begin, stop)
        return path

    def pathMapMiniComplete(self, model):
        warehouseGraph = model.warehouseGraph
        start = model.start
        end = model.end
        path = model.pathMatrix
        print("completing path matrix\n")
        nodes = warehouseGraph["nodes"]
        # path=dict()
        path[end] = dict()
        path[start] = dict()
        for begin in nodes:
            if "pick" not in begin:
                continue
            # path[begin]=dict()
            path[begin][end] = shortestPath(warehouseGraph, begin, end)
            path[end][begin] = shortestPath(warehouseGraph, end, begin)
            path[begin][start] = shortestPath(warehouseGraph, begin, start)
            path[start][begin] = shortestPath(warehouseGraph, start, begin)
        path[start][end] = shortestPath(warehouseGraph, start, end)
        path[end][start] = shortestPath(warehouseGraph, end, start)
        return path

    def setOrderLists(self, warehouseData):
        print("Manually input the itemID")
        storage = warehouseData["items"]

        orderlist = []
        cnt = 0
        while True:
            item = input("Add the itemID or type end to quit:")
            if item == "end":
                print("Order lists is " + str(orderlist))
                break
            if item in storage:
                orderlist.append(item)
                print("Added " + str(item) + " to the list")
                cnt += 1
                print("Order lists is " + str(orderlist))
            else:
                print(str(item) + " not in the storage")
            print(str(cnt) + " items in the list")
        print("")
        return orderlist
