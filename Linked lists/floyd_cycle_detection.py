class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None

    def insert_end(self,value):
        node = Node(value)
        if(self.head==None):
            self.head = node
        else:
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = node

    def insert_head(self,value):
        node = Node(value)
        if(self.head==None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def detect_cycle(self):
        if self.head == None:
            print('NO CYCLE DETECTED')
            return
        fast = slow = self.head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if(slow==fast):
                print('CYCLE DETECTED')
                return
        print('NO CYCLE DETECTED')



lis = Linkedlist()
lis.insert_head(1)
lis.insert_head(1)
lis.insert_head(2)
lis.insert_head(2)
lis.insert_head(2)
lis.insert_head(3)
lis.insert_head(3)
lis.insert_end(4)

################ creating a cycle for test ################

lis.head.next.next.next.next.next.next = lis.head.next.next.next

lis.detect_cycle()