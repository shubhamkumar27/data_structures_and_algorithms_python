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

def duplicates(lis):
    if lis.head == None:
        return
    hashtable = dict()
    pre = lis.head
    hashtable[str(pre.data)]=True
    #print(hashtable)
    temp = lis.head.next
    while(temp):
        try:
            if hashtable[str(temp.data)]:
                pre.next = temp.next
                temp = temp.next
        except:
            hashtable[str(temp.data)]=True
            pre = pre.next
            temp = temp.next
    #print(hashtable)

lis = Linkedlist()
lis.insert_end(1)
lis.insert_end(2)
lis.insert_end(2)
# lis.insert_end(4)
# lis.insert_end(5)
# lis.insert_end(6)
# lis.insert_end(7)
# lis.insert_end(8)
# lis.insert_end(9)
lis.traverse()
duplicates(lis)
lis.traverse()