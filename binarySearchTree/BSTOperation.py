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
    #This function can be used in delete node function 
    def findMin(self, root):
        current = root 
  
        # loop down to find the lefmost leaf
        while(current.left is not None): 
            current = current.left 
        # return super parent root
        return current
    
    def deleteNode(self, root, data):  #asumsikan ada objek bernama root
        if root is None:
            return root
        if data > root.data:
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
            if root.left is None:
                temp = root.right  
                root = None 
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            #if node has two children
            #first, find the minimum value
            temp = self.findMin(root.right)
            #place minimum value as root.data
            root.data = temp.data
            #the rest is on the right root so recurse again
            root.right = self.deleteNode(root.right, temp.data)  
        return root
                    
                
         
         
            
    def findMax(self, root):
        current = root
        
        while current.right is not None:
            current = current.right
                    
        return current.data
    # Function to get the count of full nodes in binary tree 
    def countFullNode(self, root): 
  
        if (root == None): 
            return 0
          
        res = 0
        if (root.left and root.right): 
            res += 1
          
        res += (self.countFullNode(root.left) + 
                self.countFullNode(root.right))  
        return res  
    # Function to get the count of leaf nodes in binary tree 
    def countLeafNode(self, node): 
        if node is None: 
            return 0 
        res = 0
        if(node.left is None and node.right is None): 
            res+=1
        res += self.countLeafNode(node.left) + self.countLeafNode(node.right) 
        return res
    # Function to get the count of both full or leaf nodes in binary tree 
    def countNonLeafNode(self, node):
        if node is None:
            return 0
        res = 0
        if (node.left and node.right is None) or (node.right and node.left is None) or (node.left and node.right):
            res += 1        
        res += self.countNonLeafNode(node.left) + self.countNonLeafNode(node.right)
        return res
    def countTotalNode(self, node):
        if node is None:
            return 0
        res = 0
        res += 1
        res += self.countTotalNode(node.left) + self.countTotalNode(node.right)
        return res  
    def findNode(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        res1 = self.findNode(root.left, data)
        if res1:
            return True
        res2 = self.findNode(root.right, data)
        return res2
    
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
    
        
            
nodeBaru = Node(50)
nodeBaru.insertData(30)
nodeBaru.insertData(20)
nodeBaru.insertData(40)
nodeBaru.insertData(70)
nodeBaru.insertData(60)
nodeBaru.insertData(80)


print("####--VALUE--####")
nodeBaru.printInorder()
print("#################")
      
print("----COUNT NODE----")
print("Count Full Node")
print(nodeBaru.countFullNode(nodeBaru))
print("Count Leaf Node")
print(nodeBaru.countLeafNode(nodeBaru))
print("Count Non leaf Node")
print(nodeBaru.countNonLeafNode(nodeBaru))
print("Count Total Node")
print(nodeBaru.countTotalNode(nodeBaru))

print()
print("Find maximum value")
print(nodeBaru.findMax(nodeBaru))
print()

print("----DELETE NODE----")
nodeBaru.deleteNode(nodeBaru, 20)   
nodeBaru.deleteNode(nodeBaru, 30)   
nodeBaru.deleteNode(nodeBaru, 50)
nodeBaru.deleteNode(nodeBaru, 70)   

print("####--VALUE--####")
nodeBaru.printInorder()
print("#################")
      
print("----COUNT NODE----")
print("Count Full Node")
print(nodeBaru.countFullNode(nodeBaru))
print("Count Leaf Node")
print(nodeBaru.countLeafNode(nodeBaru))
print("Count Non leaf Node")
print(nodeBaru.countNonLeafNode(nodeBaru))
print("Count Total Node")
print(nodeBaru.countTotalNode(nodeBaru))

print()
print("Find maximum value")
print(nodeBaru.findMax(nodeBaru))
print()

print("####--VALUE--####")
nodeBaru.printInorder()
print("#################")
      
print(nodeBaru.findNode(nodeBaru, 80))
      






        
