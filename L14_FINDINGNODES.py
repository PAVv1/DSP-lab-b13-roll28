  
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
            pass


    def findvalue(self, lvalue):
        if lvalue < self.data:
            if self.left is None:
                return str(lvalue)+" is not Found"
            return self.left.findvalue(lvalue)
        elif lvalue > self.data:
            if self.right is None:
                return str(lvalue)+" is not Found"
            return self.right.findvalue(lvalue)
        else:
            return str(self.data) + " is found"

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


root = Node(17)
n = int(input("range: "))
print("Enter elements to add:")
for i in range(n):
    root.insert(int(input()))

print(root.findvalue(42))
print(root.findvalue(17))