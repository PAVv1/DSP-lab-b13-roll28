#l8_linkedlist1
#121910313028
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class DoublyLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,data):
        newNode=Node(data)
        if(self.head==None):
            self.head=self.tail=newNode
            self.head.previous=None
            self.tail.next=None
        else:
            self.tail.next=newNode
            newNode.previous=self.tail
            self.tail=newNode
            self.tail.next=None

    def display(self):
        current=self.head
        if(self.head==None):
            print("list is empty")
            return
        print("nodes of doubly linked list: ")
        while(current!=None):
            print(current.data)
            current=current.next


doublelist=DoublyLinkedlist()
doublelist.addNode(1)
doublelist.addNode(2)
doublelist.addNode(3)
doublelist.addNode(5)
doublelist.addNode(4)

doublelist.display()