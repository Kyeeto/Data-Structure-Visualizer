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

    def delete_node(self, node, val):
        if node is None:
            return None

        if val < node.val:
            node.left = self.delete_node(node.left, val)
        elif val > node.val:
            node.right = self.delete_node(node.right, val)
        else:
            if node.left is None and node.right is None:
                self.size -= 1
                return None
            elif node.left is None:
                self.size -= 1
                return node.right
            elif node.right is None:
                self.size -= 1
                return node.left
            else:
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.val = successor.val
                node.right = self.delete_node(node.right, successor.val)
        return node
    def delete(self, val):
        self.root = self.delete_node(self.root, val)

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

    