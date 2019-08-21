class Node():
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

class Binarytrees():
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if (self.root==None):
            self.root = node
            