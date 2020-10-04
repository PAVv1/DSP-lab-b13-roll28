"""PAVAN SAI .V]
   121910313028"""
#Create a linked list with few sample nodes as static inputs
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printv = self.head
        while printv:
            print (printv.data)
            printv = printv.next
#Programming execution starts here
list = SLinkedList()
list.head = Node("mon")
k2 = Node("tue")
w3 = Node("wed")
w4= Node("thu")
w5=Node("fri")
w6=Node("sat")
w7=Node("sun")
# Link first Node to second node
list.head.next = k2
# Link second Node to third node
k2.next = w3
w3.next = w4
w4.next=w5
w5.next=w6
w6.next=w7
list.listprint()
   