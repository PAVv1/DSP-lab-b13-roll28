#l7_linkedlist2
#121910313028
#creating a class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def input(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next

        temp = None

    def printList(self):
        temp = self.head
        while (temp):
            print(" %d" % (temp.data)),
            temp = temp.next

linklist = LinkedList()
linklist.input(5)
linklist.input(1)
linklist.input(8)
linklist.input(4)

print("Created Linked List: ")
linklist.printList()
linklist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
linklist.printList()