class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        t=self.head
        while t.next:
            t=t.next
        t.next=new
        return
    def pop(self):
        if self.head is None:
            print("Underflow")
            return
        p=None
        t=self.head
        while t.next:
            p=t
            t=t.next
        l=t.data
        p.next=None
        t=None
        return l
    def printStack(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next
        print()
        return
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.pop())
s.printStack()