  
#l7_linkedlist5
#121910313028
#creating a class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def input(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

linklist = LinkedList()
linklist.input(2)
linklist.input(4)
linklist.input(6)
linklist.input(8)
linklist.input(10)
print("Given Linked List:")
linklist.printList()
linklist.reverse()
print("\nReversed Linked List:")
linklist.printList()