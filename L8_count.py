#l8_count
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
    def count_nodes(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count
d=DoublyLinkedList()
d.append(10)
d.append(20)
d.append(30)
print(d.count_nodes())