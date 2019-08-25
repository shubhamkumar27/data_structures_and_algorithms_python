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


    def preorder(self,root):
        if root == None:
            return
        while(root):
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
            break

    def inorder(self,root):
        if root == None:
            return
        while(root):
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            break

    def postorder(self,root):
        if root == None:
            return
        while(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
            break

    def levelorder(self,root):
        if root == None:
            return
        q = [root]
        while(len(q)>0):
            n = q.pop(0)
            print(n.data)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

tree = BST()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(2)
tree.preorder(tree.root)
print('****************************')
tree.inorder(tree.root)
print('****************************')
tree.postorder(tree.root)
print('****************************')
tree.levelorder(tree.root)