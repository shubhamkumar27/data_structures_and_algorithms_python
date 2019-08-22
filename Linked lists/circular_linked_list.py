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
            node.next = self.head

    def insert_head(self,value):
        node = Node(value)
        if(self.head==None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def traverse(self):
        if self.head == None:
            return None
        cur = self.head
        print('Elements are :', end=' ')
        while(cur.next!=self.head):
            print(cur.data,end=' ')
            cur = cur.next
        print(cur.data)

    def delete_end(self):
        if(self.head==None):
            return
        else:
            cur = self.head
            while(cur.next.next!=self.head):
                cur = cur.next
            cur.next = self.head

    # def delete_head(self):
    #     if(self.head==None):
    #         return
    #     else:
    #         self.head = self.head.next

    def delete_val(self,value):
        if(self.head==None):
            return
        elif(self.head.data == value):
            self.head = self.head.next
        else:
            pre = self.head
            cur = self.head.next
            while(cur!=self.head):
                if(cur.data==value):
                    if(cur.next==None):
                        pre.next = self.head
                    else:
                        pre.next = cur.next
                    break
                else:
                    pre = cur
                    cur = cur.next
            if(cur == None):
                print('Element not found')

lis = Linkedlist()
lis.insert_head(1)
lis.insert_head(1)
lis.insert_head(2)
lis.insert_head(2)
lis.insert_head(9)
lis.insert_head(3)
lis.insert_head(3)
lis.insert_end(4)
#print('Length of list is : '+ str(lis.length()))
lis.traverse()
lis.delete_end()
lis.traverse()
lis.delete_val(9)
lis.traverse()
