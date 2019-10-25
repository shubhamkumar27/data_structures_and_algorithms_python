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

    def length(self):
        if self.head == None:
            return 0
        cur = self.head
        i = 0
        while(cur):
            i +=1
            cur = cur.next
        return i

def traverse(cur):
    # if self.head == None:
    #     return None
    # cur = self.head
    print('Elements are :', end=' ')
    while(cur):
        print(cur.data,end=' ')
        cur = cur.next
    print()

############## RECURSIVE SOLUTION ################
def reverse_k(head,k):
    if lis.head==None:
        return
    cur = head
    pre = None
    i=0
    while(cur and i<k):
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
        i+=1
    if cur:
        head.next = reverse_k(cur,k)
    return pre

############# ITERATIVE SOLUTION ##################
def rev_k_iter(head,k):
    jump = Node(0)
    dummy = jump
    l = head
    r = l
    #dummy.next = r
    while True:
        count = 0
        while count<k and r:
            r = r.next
            count += 1
        if count==k:
            pre , cur = r, l
            for _ in range(k):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            jump.next = pre
            jump = l
            l=r
        else:
            return dummy.next


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
traverse(lis.head)
head = rev_k_iter(lis.head,3)
traverse(head)