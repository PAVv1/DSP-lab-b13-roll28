  
class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def printstack(self):
        print(self.items)

s=stack()
n=int(input())
for i in range(n):
    ele=input()
    s.push(ele)
s.printstack()
s.push('kapil')
s.printstack()
print(s.peek())
print(s.pop())
