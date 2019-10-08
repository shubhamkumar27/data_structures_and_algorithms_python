class Node():
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None

    def insert(self,value):
        node = Node(value)
        if(self.head==None):
            self.head = node
        else:
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = node

    def traverse(self):
        if self.head == None:
            return None
        cur = self.head
        print('Elements are :', end=' ')
        while(cur):
            print(cur.data,end=' ')
            cur = cur.next
        print()

def merge_reverse(l1,l2):
    if l1==None and l2==None: return None
    t1 = l1.head
    t2 = l2.head
    result = None
    while(t1 != None and t2 != None):
        if t1.data <= t2.data:
            temp = t1.next
            t1.next = result
            result = t1
            t1 = temp
        else:
            temp = t2.next
            t2.next = result
            result = t2
            t2 = temp
    while(t1 != None):
        temp = t1.next
        t1.next = result
        result = t1
        t1 = temp
    while(t2 != None):
        temp = t2.next
        t2.next = result
        result = t2
        t2 = temp
    r = Linkedlist()
    r.head = result
    r.traverse()

l1 = Linkedlist()
l2 = Linkedlist()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(5)
l1.insert(7)
l1.insert(9)
l2.insert(0)
l2.insert(4)
l2.insert(6)
merge_reverse(l1,l2)
