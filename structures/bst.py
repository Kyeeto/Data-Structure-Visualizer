"""

    A binary search tree implementation using a Node class, keeping track of the root and length

    Methods:
    insert(val)          : Inserts a node with value "val" into the tree, ignores duplicates
    delete(val)          : Removes the node with value "val" from the tree, does nothing if not found
    search(val)          : Returns the node containing "val", returns None if not found
    in_order()           : Returns a list of all values in sorted (ascending) order
    pre_order()          : Returns a list of all values in pre-order (node, left, right)
    post_order()         : Returns a list of all values in post-order (left, right, node)
    find_min()           : Returns the smallest value in the tree, returns None if empty
    find_max()           : Returns the largest value in the tree, returns None if empty
    is_empty()           : Returns True if the tree has no nodes, False otherwise
    size()               : Returns the number of nodes in the tree
    clear()              : Removes all nodes and resets the tree

    """

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree(): 
    def __init__(self):
        self.root = None
        self.length = 0

    def insertNode(self, node, val):
        if node is None:
            newNode = Node(val)
            self.length +=1
            return newNode
        if val < node.val:
            node.left = (self.insert_node(node.left, val))
        else:
            node.right = (self.insert_node(node.right, val))
        return node
    def insert(self, val):
        self.root = self.insertNode(self.root, val)

    def deleteNode(self, node, val):
        if node is None:
            return None

        if val < node.val:
            node.left = self.delete_node(node.left, val)
        elif val > node.val:
            node.right = self.delete_node(node.right, val)
        else:
            if node.left is None and node.right is None:
                self.length -= 1
                return None
            elif node.left is None:
                self.length -= 1
                return node.right
            elif node.right is None:
                self.length -= 1
                return node.left
            else:
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.val = successor.val
                node.right = self.delete_node(node.right, successor.val)
        return node
    def delete(self, val):
        self.root = self.deleteNode(self.root, val)

    def search(self, val):
        current = self.root
        while current != None:
            if val == current.val:
                return current
            elif val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
        return None
    
    def inOrder(self):
        result = []
        self.inOrderHelper(self.root, result)
        return result
    def inOrderHelper(self, node, result):
        if (node is None):
            return
        self.inOrderHelper(node.left, result)
        result.append(node.val)
        self.inOrderHelper(node.right, result)

    def pre_order(self):
        result = []
        self.preOrderHelper(self.root, result)
        return result
    def preOrderHelper(self, node, result):
        if (node is None):
            return
        result.append(node.val)
        self.preOrderHelper(node.left, result)
        self.preOrderHelper(node.right, result)

    def post_order(self):
        result = []
        self.postOrderHelper(self.root, result)
        return result
    def postOrderHelper(self, node, result):
        if (node is None):
            return
        self.postOrderHelper(node.left, result)
        self.postOrderHelper(node.right, result)
        result.append(node.val)

    def is_empty(self):
        return self.root == None

    def size(self):
        return self.length

    def clear(self):
        self.root = None
        self.length = 0

    def findMin(self):
        if self.root == None:
            return None
        current = self.root
        while current.left != None:
            current = current.left
        return current.val

    def findMax(self):
        if self.root == None:
            return None
        current = self.root
        while current.right != None:
            current = current.right
        return current.val

    