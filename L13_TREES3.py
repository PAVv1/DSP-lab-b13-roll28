  
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(rootval):
    if rootval:
        printInorder(rootval.left)
        print(rootval.val),
        printInorder(rootval.right)


def printPostorder(rootval):
    if rootval:
        printPostorder(rootval.left)
        printPostorder(rootval.right)
        print(rootval.val)


def printPreorder(rootval):
    if rootval:
        print(rootval.val)
        printPreorder(rootval.left)
        printPreorder(rootval.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.left.left.left=Node(8)
root.left.left.right=Node(9)
root.right.left.left=Node(10)
root.right.right.left=Node(11)
root.right.right.right=Node(12)

print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)