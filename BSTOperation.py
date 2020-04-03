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
    def findMin(self, root):
        current = root 
  
        # loop down to find the lefmost leaf
        while(current.left is not None): 
            current = current.left 
        # return super parent root
        return current.data 
    
    def deleteNode(self, root, data):  #asumsikan ada objek bernama root
        if root is None:
            return root
        elif data > root.data:
            root.right = self.deleteNode(root.right, data)
        elif data < root.data:
            root.left = self.deleteNode(root.left, data)
        else:
            '''
            using 4 probabilities
            1. if node has no child
            2. if node has 1 child at right
            3. if node has 1 child at left
            4. if node has two childs 
            '''            
            #If node has only one child or no child
            if root.right is None:
                temp = root.right  
                root = None 
                return temp
            else:
                temp = root.left
                root = None
                return temp
            
            #if node has two children
            #first, find the minimum value
            temp = self.findMin(root)
            #place minimum value as root.data
            root.data = temp.data
            #the rest is on the right root so recurse again
            root.right = self.deleteNode(root.right, temp.data)      
            
            
            
    # Left - Root - Right             
    def printInorder(self):
        if self.left:
            self.left.printInorder()
        print(self.data)
        if self.right:
            self.right.printInorder()
    
    # Left - Right - Root
    def printPostorder(self):
        if self.left:
            self.left.printInorder()
        if self.right:
            self.right.printInorder()
        print(self.data)
        
    # Root - Left - Right
    def printPreorder(self):
        print(self.data)
        if self.left:
            self.left.printInorder()
        if self.right:
            self.right.printInorder()
            
nodeBaru = Node(10)
nodeBaru.insertData(9)
nodeBaru.insertData(12)
nodeBaru.insertData(13)
nodeBaru.insertData(11)
nodeBaru.deleteNode(nodeBaru, 12)

nodeBaru.printInorder()
        
