from Binary_serch_tree import BST

####### function to delete ########

def delete(root,value):
    if root == None:
        return
    elif value < root.data:
        root.left = delete(root.left,value)
    elif value > root.data:
        root.right = delete(root.right,value)
    else:
        if(root.left==None and root.right==None):
            root = None
        elif root.left == None:
            root = root.right
        elif root.right == None:
            root = root.left
        else:
            min = find_min(root.right)
            root.data = min.data
            root.right = delete(root.right,min.data)
    return root

def find_min(root):
    while(root.left!=None):
        root = root.left
    return root

tree = BST()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(2)
tree.inorder(tree.root)
delete(tree.root,7)
tree.inorder(tree.root)