  
#l8_search
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
    def search(self,key):
        cur=self.head
        while cur:
            if cur.data==key:
                return True
            cur=cur.next
        return False
d=DoublyLinkedList()
n=int(input("enter no. of elements to append "))
for i in range(n):
    d.append(int(input()))
k=int(input("Enter the element to search "))
print(d.search(k))