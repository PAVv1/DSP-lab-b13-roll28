"""PAVAN SAI .V
   121910313028"""
#Create a linked list with few sample nodes as static inputs
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def _init_(self):
        self.head = None

    def listprint(self):
        printv = self.head
        while printv is not None:
            print (printv.data)
            printv = printv.next
#Programming execution starts here
list = SLinkedList()
list.head = Node(1)
w2 = Node(2)
w3 = Node(3)
w4= Node(4)
w5=Node(5)
# Link first Node to second node
list.head.next = w2
# Link second Node to third node
w2.next = w3
w3.next = w4
w4.next=w5
list.listprint()