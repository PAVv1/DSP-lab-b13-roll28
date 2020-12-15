#l8_insertatanypos
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
    def insert_at_position(self,data,pos):
        if not self.head:
            return
        if pos==1:
            self.prepend(data)
            return
        else:
            new=Node(data)
            prev=None
            count=1
            temp=self.head
            while temp and pos!=count:
                prev=temp
                temp=temp.next
                count+=1
            prev.next=new
            new.prev=prev
            new.next=temp
            temp.prev=new
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
    def prepend(self,data):
        if self.head is None:
            new=Node(data)
            new.next=self.head
            self.head=new
        else:
            new=Node(data)
            self.head.prev=new
            new.next=self.head
            self.head=new
d=DoublyLinkedList()
d.append(10)
d.append(20)
d.append(30)
d.insert_at_position(15,3)
d.print_list()