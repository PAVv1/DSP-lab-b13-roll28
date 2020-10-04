"""PAVAN SAI. V
121910313028"""
#Linked list with user input
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
l=LinkedList()
n=int(input("size:"))
for i in range(n):
    data=int(input())
    l.append(data)
l.disp()            