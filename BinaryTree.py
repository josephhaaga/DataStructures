# Trees are composed of nodes
# Nodes have a value, left pointer, and right pointer.

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.value = val

class Tree:
	def __init__(self):
		self.root = None

	def DeleteTree(self):
		self.root = None

	def IsEmpty(self):
		return self.root == None

	def PrintTree(self):
		if(self.root != None):
			self._PrintTree(self.root)

	def _PrintTree(self, node):
		if(node != None):
			self._PrintTree(node.left)
			print(str(node.value) + " ")
			self._PrintTree(node.right)

	def find(self, val):
		if(self.root != None):
			return self._find(val, self.root)
		else:
			return None

	def _find(self, val, root):
		if(val == node.value):
			return node
		elif(val < node.value and node.left != None):
			self._find(val, node.left)
		elif(val > node.value and node.right != None):
			self._find(val, node.right)


