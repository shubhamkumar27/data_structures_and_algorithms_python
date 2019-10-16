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

    def reverse(self):
        if self.head == None or self.head.next == None:
            return
        head = self.head
        tail = None
        while(head):
            t = head.next
            head.next = tail
            tail = head
            head = t
        self.head = tail

def addition(l1,l2):
    if not l1 : return l2
    if not l2 : return l1
    l1.reverse()
    l2.reverse()
    temp1 = l1.head
    temp2 = l2.head
    s = Linkedlist()
    carry = 0
    i=0
    while temp1 or temp2 or carry != 0 :
        d1 = temp1.data if temp1 else 0
        d2 = temp2.data if temp2 else 0
        #print(i,end='->')
        summ = d1 + d2 + carry
        sdata = (summ)%10
        carry = (summ)//10
        #print(sdata)
        s.insert(sdata)
        if temp1 : temp1 = temp1.next
        if temp2 : temp2 = temp2.next
        i+=1
    s.reverse()
    s.traverse()

l1 = Linkedlist()
l1.insert(5)
# l1.insert(4)
# l1.insert(3)
l1.traverse()
l2 = Linkedlist()
# l2.insert(9)
# l2.insert(4)
l2.insert(5)
l2.traverse()
addition(l1,l2)