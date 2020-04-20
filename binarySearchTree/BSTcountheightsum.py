class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insertData(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insertData(data)
        elif data >  self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insertData(data)
        else:
            self.data = data
    #Mencari banyak leaf (hitungLeaf)
    def countLeafNode(self, node): 
        if node is None: 
            return 0 
        res = 0
        if(node.left is None and node.right is None): 
            res+=1
        res += self.countLeafNode(node.left) + self.countLeafNode(node.right) 
        return res  
    #Menghitung tinggi tree
    def countHeightTree(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.countHeightTree(root.left), self.countHeightTree(root.right))
    #Menghitung sum dari semua node
    def sumAllNode(self, root):
        if root is None: 
            return 0 
        else:
            res = 0
            if (root.left or root.right) or (root.left is None and root.right is None):
                res+=1
            res += self.sumAllNode(root.left) + self.sumAllNode(root.right)
            return res

nodeBaru = Node(50)
nodeBaru.insertData(10)
nodeBaru.insertData(60)
nodeBaru.insertData(20)
nodeBaru.insertData(30)
nodeBaru.insertData(15)
nodeBaru.insertData(12)
nodeBaru.insertData(90)
nodeBaru.insertData(45)
nodeBaru.insertData(23)
nodeBaru.insertData(67)
print(nodeBaru.countLeafNode(nodeBaru)) 
print(nodeBaru.countHeightTree(nodeBaru))
print(nodeBaru.sumAllNode(nodeBaru))

