class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree(): 
    def __init__(self):
        self.root = None
        self.size = 0

    def insert_node(self, node, val):
        if node is None:
            newNode = Node(val)
            self.size +=1
            return newNode
        if val < node.val:
            node.left = (self.insert_node(node.left, val))
        else:
            node.right = (self.insert_node(node.right, val))
        return node
    def insert(self, val):
        self.root = self.insert_node(self.root, val)

    def delete(self):
        pass 

    def search(self):
        pass
    
    def inOrder(self):
        pass

    def preOrder(self):
        pass

    def postOrder(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

    def clear(self):
        pass

    def findMin(self):
        pass

    def findMax(self):
        pass

    