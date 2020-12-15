#l8_linkedlist2
#121910313028
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class starting:
    def __init__(self):
        self.head=None
        self.tail=None

    def addatstart(self,data):
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
        print("adding node at beginning of doubly linked list: ")
        while(current!=None):
            print(current.data)
            current=current.next
        print()


doublelist=starting()
doublelist.addatstart(1)
doublelist.display()
doublelist.addatstart(2)
doublelist.display()
doublelist.addatstart(3)
doublelist.display()
doublelist.addatstart(5)
doublelist.display()
doublelist.addatstart(4)
doublelist.display()