class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue():
    def __init__(self):
        self.head = None

    def enqueue(self,value):
        node = Node(value)
        if(self.head==None):
            self.head = node
        else:
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = node

    def dequeue(self):
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

list = Queue()
list.enqueue(1)
list.enqueue(2)
list.enqueue(3)
list.enqueue(4)
list.enqueue(5)
list.traverse()
list.dequeue()
list.traverse()