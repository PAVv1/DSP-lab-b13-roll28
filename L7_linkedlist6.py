#l7_linkedlist6
#121910313028
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def search(self,key):
        temp=self.head
        while temp:
            if temp.data==key:
                print("element found")
                return
            temp=temp.next
        print("Element not found ")
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
l=LinkedList()
n=int(input("Enter how many numbers you want to add "))
for i in range(n):
    data=int(input("enter data item: "))
    l.append(data)
l.print_list()
k=int(input("Enter the element to search: "))
l.search(k)