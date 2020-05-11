from collections import defaultdict 

arr = []


for i in range(6):
    col = []
    for j in range(6):
        col.append(0)
    arr.append(col)
#tidak bisa lewat
arr[0][1] = 2
arr[1][1] = 2
arr[4][1] = 2
arr[5][1] = 2
arr[0][2] = 2
arr[0][3] = 2
arr[1][3] = 2
arr[2][3] = 2
arr[3][3] = 2
arr[4][3] = 2
arr[0][4] = 2
arr[4][4] = 2
arr[2][5] = 2
#bisa lewat
arr[0][0] = 1
arr[1][0] = 1
arr[3][0] = 1
arr[4][0] = 1
arr[2][1] = 1
arr[3][1] = 1
arr[1][2] = 1
arr[2][2] = 1
arr[3][2] = 1
arr[4][2] = 1
arr[5][2] = 1
arr[5][3] = 1
arr[1][4] = 1
arr[2][4] = 1
arr[3][4] = 1
arr[5][4] = 1
arr[1][5] = 1
arr[3][5] = 1
arr[4][5] = 1
arr[5][5] = 1
#mulai
arr[2][0] = 0
#selesai
arr[5][0] = 3
arr[0][5] = 3

for i in range(6):
    print(arr[i])



class Graph():
    def __init__(self):
        self.value = defaultdict(list)

    def addConnection(self, parent, child):
        self.value[parent].append(child)

    def DFS(self, start):
        visited = [start]
        stack = [start]
        print(start, end = " ")
        while stack:
            s = stack[-1]
            if any([item for item in self.value[s] if item not in visited]):
                for item in [item for item in self.value[s] if item not in visited]:
                        stack.append(item)
                        visited.append(item)
                        print(item, end= " ")
                        break
            else:
                stack.pop()

    def BFS(self, start):
        visited = [start]
        queue = [start]
        while queue:
            x = queue.pop(0)
            print(x, end= " ")
            for item in self.value[x]:
                if item not in visited:
                    queue.append(item)
                    visited.append(item)

#bangun the graph
g=Graph()
g.addConnection(arr[2][0],arr[1][0])
g.addConnection(arr[2][0],arr[2][1])
g.addConnection(arr[2][0],arr[3][0])
g.addConnection(arr[1][0],arr[0][0])
g.addConnection(arr[2][1],arr[2][2])
g.addConnection(arr[2][1],arr[3][1])
g.addConnection(arr[3][0],arr[4][0])
g.addConnection(arr[4][0],arr[5][0])
g.addConnection(arr[2][2],arr[1][2])
g.addConnection(arr[2][2],arr[3][2])
g.addConnection(arr[3][2],arr[4][2])
g.addConnection(arr[4][2],arr[5][2])
g.addConnection(arr[5][2],arr[5][3])
g.addConnection(arr[5][3],arr[5][4])
g.addConnection(arr[5][4],arr[5][5])
g.addConnection(arr[5][5],arr[4][5])
g.addConnection(arr[4][5],arr[3][5])
g.addConnection(arr[3][5],arr[3][4])
g.addConnection(arr[3][4],arr[2][4])
g.addConnection(arr[2][4],arr[1][4])
g.addConnection(arr[1][4],arr[1][5])
g.addConnection(arr[1][5],arr[0][5])


#Explor graph
g.DFS(arr[2][0])
print("\n")
g.BFS(arr[2][0])
    



        
        
