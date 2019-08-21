class Node():
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

class Binarytrees():
    def __init__(self):
        self.root = None

    def insert(self,arr):
        self.root = self.insert1(arr=arr)

    def insert1(self,arr, root=None, i = 0):
        n=len(arr)
        if i < n:
            temp = Node(arr[i])
            root = temp
            # insert left child
            root.left = self.insert1(arr, root.left, 2 * i + 1)
            # insert right child
            root.right = self.insert1(arr, root.right, 2 * i + 2)
        return root

    def preorder(self,root = None):
        if self.root == None:
            return
        if root == None:
            root = self.root
        while(root):
            print(root.data)
            if (root.left):
                self.preorder(root.left)
            if (root.right):
                self.preorder(root.right)
            break

l = [1,2,3,4,5,6,7,8,9]
tree = Binarytrees()
tree.insert(l)
tree.preorder()
