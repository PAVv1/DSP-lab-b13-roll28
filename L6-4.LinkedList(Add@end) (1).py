"""PAVAN SAI.V
121910313028"""
#Inserting a node at the end of the Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        if self.tail is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
    def disp(self):
        cur=self.head 
        while cur is not None:
            print(cur.data,end=" ")
            cur=cur.next
    def add_at_end(self,data):
        cur=self.head
        while cur.next is not None:
            cur=cur.next 
        new=Node(data)    
        cur.next=new
        new.next=None
#program execution starts here            
l=LinkedList()
n=int(input("size:"))
print("elements:")
for i in range(n):
    data=int(input())
    l.append(data)
k=int(input("element to add at ending"))    
l.add_at_end(k) #calling add at beginning method to add element  
l.disp()        