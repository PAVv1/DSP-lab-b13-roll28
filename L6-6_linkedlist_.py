#Search the node

#Class Node
class node:
	def _init_(self,data):
		self.data = data
		self.next = None
#Linked List Class
class LinkedList:
	def _init_(self):
		self.head = None
		self.tail =None

	#adding element
	def append(self,data):
		new_node = node(data)
		if self.head == None and self.tail == None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

	#printing elements
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Linked List: ",ele)

	#Search element function
	def Search(self,data):
		temp = self.head
		while temp:
			if temp.data == data: 
				return True
			temp = temp.next
		return False

LL = LinkedList()
n = int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
	k = int(input())
	LL.append(k)

print("Before: ")
LL.display()

v = int(input("Element to be searched: "))
print(LL.Search(v))