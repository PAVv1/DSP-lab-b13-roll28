class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data, n):
        if data not in self.stack and len(self.stack) <= n:
            self.stack.append(data)
            return
        print("OverFlow")
        return

    def pop(self):
        if len(self.stack) > 0:
            l = self.stack[-1]
            self.stack.pop()
            return l
        print("Underflow")
        return

    def printStack(self):
        for i in self.stack:
            print(i, end=" ")
        return


t = True
l = int(input("Enter size of stack "))
s = Stack()
while t:

    n = int(input("Enter the operation you want to perform 1.push 2.pop 3.Display 4.exit "))
    if n == 1:
        s.push(int(input("enter element ")), l)
    elif n == 2:
        print(s.pop())
    elif n == 3:
        s.printStack()
    elif n == 4:
        t = False
    else:
        print("Enter a valid input ")
