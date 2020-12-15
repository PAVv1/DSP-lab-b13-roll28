  
#l8_delete
class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def append(self,data):
        if self.head is None:
            new=Node(data)
            self.head=new
        else:
            new=Node(data)
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new
            new.prev=cur
    def delete(self,key):
        cur=self.head
        while cur:
            if cur.data==key and cur==self.head:
                if cur.next==None:
                    cur=None
                    self.head=None
                    return
                else:
                    nxt=cur.next
                    cur.next=None
                    nxt.prev=None
                    cur=None
                    self.head=nxt
                    return
            elif cur.data==key:
                if cur.next:
                    nxt=cur.next
                    previ=cur.prev
                    previ.next=nxt
                    nxt.prev=previ
                    cur.next=None
                    cur.prev=None
                    cur=None
                    return
                else:
                    previ=cur.prev
                    previ.next=None
                    cur.next=None
                    cur.prev=None
                    return
            cur=cur.next
d=DoublyLinkedList()
n=int(input("enter no. of elements to append "))
for i in range(n):
    d.append(int(input()))
k=int(input("Enter the element to delete "))
d.delete(k)
d.print_list()