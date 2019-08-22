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

    def insert_pos(self,value,position):
        length = self.length()
        if (position > length or position < 1):
            print(str(position)+' position does not exist')
            return
        else:
            node = Node(value)
            if(self.head==None):
                self.head = node
            else:
                i=0
                cur = self.head
                while(i<position-2):
                    cur = cur.next
                    i+=1
                node.next = cur.next
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

    def length(self):
        if self.head == None:
            return 0
        cur = self.head
        i = 0
        while(cur):
            i +=1
            cur = cur.next
        return i

########################################################################
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

#################################################################3

lis = Linkedlist()
lis.insert_head(1)
lis.insert_head(1)
lis.insert_head(2)
lis.insert_head(2)
lis.insert_head(2)
lis.insert_head(3)
lis.insert_head(3)
lis.insert_pos(7,7)
lis.insert_pos(9,7)
lis.insert_pos(8,7)
lis.insert_end(4)
print('Length of list is : '+ str(lis.length()))
lis.traverse()
lis.reverse()
lis.traverse()
