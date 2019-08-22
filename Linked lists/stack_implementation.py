class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        if (self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if (self.head == None):
            return
        else:
            self.head = self.head.next

    def traverse(self):
        if self.head == None:
            return None
        cur = self.head
        print('Elements are :', end=' ')
        while (cur):
            print(cur.data, end=' ')
            cur = cur.next
        print()

list = Stack()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)
list.traverse()
list.pop()
list.traverse()