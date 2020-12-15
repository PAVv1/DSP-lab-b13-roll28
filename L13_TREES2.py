class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintingTree(self):
        if self.left:
            self.left.PrintingTree()
        print( self.data),
        if self.right:
            self.right.PrintingTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(13)
root.insert(33)
root.insert(53)
root.insert(300)
root.insert(3)
root.insert(77)
root.insert(4)
root.insert(303)
root.insert(305)

root.PrintingTree()