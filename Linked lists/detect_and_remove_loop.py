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
    
    def traverse(self):
        if self.head == None:
            return None
        cur = self.head
        print('Elements are :', end=' ')
        while(cur):
            print(cur.data,end=' ')
            cur = cur.next
        print()

####################### DETECTING CYCLE ############################
def detect_cycle(l):
    if l.head == None:
        print('NO CYCLE DETECTED')
        return
    fast = slow = l.head
    while(fast!=None and fast.next!=None):
        slow = slow.next
        fast = fast.next.next
        if(slow==fast):
            print('CYCLE DETECTED')
            rem_cycle(fast,l)
            return
    print('NO CYCLE DETECTED')

######################## REMOVE CYCLE #################################
def rem_cycle(p1,l):
    p2 = l.head
    while(p1 != p2):
        p1 = p1.next
        p2 = p2.next
    print('First element of loop is : ',p1.data)
    while(p2.next != p1):
        p2 = p2.next
    p2.next = None

    ####### CHECK FOR LOOP AGAIN #######
    detect_cycle(l)



lis = Linkedlist()
lis.insert_end(1)
lis.insert_end(2)
lis.insert_end(3)
lis.insert_end(4)
lis.insert_end(5)
lis.insert_end(6)
lis.insert_end(7)
lis.insert_end(8)
lis.insert_end(9)
lis.traverse()

################ creating a cycle for test ################

lis.head.next.next.next.next.next.next.next = lis.head.next.next.next.next

################ checking for cycle detection ##################

detect_cycle(lis)