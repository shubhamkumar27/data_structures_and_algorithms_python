class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        root = self.root
        if root==None:
            self.root = node
            return
        while(True):
            if(value<=root.data):
                if(root.left == None):
                    root.left = node
                    break
                else:
                    root = root.left
            else:
                if root.right == None:
                    root.right = node
                    break
                else:
                    root = root.right

    def lca(self, root, v1, v2):
        if root.data > v1 and root.data > v2:
            root = self.lca(root.left, v1, v2)
        if root.data < v1 and root.data < v2:
            root = self.lca(root.right, v1, v2)
        return root.data


tree = BST()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(2)
print(tree.lca(tree.root,2,10))
