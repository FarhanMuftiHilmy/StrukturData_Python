n = int(input())
ls_value = list(map(int,input().split()))
dkey = int(input())
class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
def insert(node, key): 
  
    # If the tree is empty, return a new node 
    if node is None:    
        return Node(key) 
  
    # Otherwise recur down the tree 
    if key < node.key: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
  
    # return the (unchanged) node pointer 
    return node 
         
def deleteNode(root, dkey):
    # if root doesn't exist, just return it
	if not root: 
		return root
	# Find the node in the left subtree	if key value is less than root value
	if root.key > dkey: 
		root.left = deleteNode(root.left, dkey)
	# Find the node in right subtree if key value is greater than root value, 
	elif root.key < dkey: 
		root.right= deleteNode(root.right, dkey)
	# Delete the node if root.value == key
	else: 
	# If there is no right children delete the node and new root would be root.left
		if not root.right:
			return root.left
	# If there is no left children delete the node and new root would be root.right	
		if not root.left:
			return root.right
  # If both left and right children exist in the node replace its value with 
  # the minmimum value in the right subtree. Now delete that minimum node
  # in the right subtree
		temp_key = root.right
		mini_key = temp_key.key
		while temp_key.left:
			temp_key = temp_key.left
			mini_key = temp_key.key
	# Replace value	
		root.key = mini_key
  # Delete the minimum node in right subtree
		root.right = deleteNode(root.right,root.key)
	return root

# A utility function to do inorder traversal of BST 
# Root -> Left ->Right
def printPreorder(root): 
    if root is not None: 
        
        print(root.key, end=" ") 
        printPreorder(root.left) 
        printPreorder(root.right) 
        

root = None
for i in range(n):
    root = insert(root, ls_value[i])
deleteNode(root, dkey)
printPreorder(root)



