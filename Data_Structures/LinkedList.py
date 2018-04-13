# A list of elements
# Each element contains a value, and a pointer to the next item (Singly-linked list)

class Node:
	def __init__(self, val, next=None):
		self.value = val 
		self.next = next 

class LinkedList:
	def __init__(self):
		self.head = None
	def Print(self):
		node = self.head
		while(node != None):
			print(str(node.value)+" "),
			node = node.next
		return None
	def Size(self):
		size = 0
		if(self.head != None):
			node = self.head
			while(node != None):
				size = size + 1
				node = node.next
		return size
	def Insert(self, val):
		if(self.head == None):
			self.head = Node(val)
		else:
			node = self.head
			while(node.next != None):
				node = node.next
			node.next = Node(val)

		return None
	def Search(self, target):
		node = self.head
		while(node != None):
			if(node.value == target):
				return node	
			node = node.next	
					
	
	def Delete(self):
		return None
