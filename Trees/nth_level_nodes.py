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
                if(root.right == None):
                    root.right = node
                    break
                else:
                    root = root.right

    def levelnodes(self,root,n):
        if root == None:
            return
        if n==0:
            print(root.data)
            return
        else:
            self.levelnodes(root.left,n-1)
            self.levelnodes(root.right,n-1)

tree = BST()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(2)
tree.levelnodes(tree.root,2)