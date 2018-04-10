import unittest
import BinaryTree

class MyTest(unittest.TestCase):
	def testIsEmpty(self):
		t = BinaryTree.Tree()
		self.assertEqual(t.IsEmpty(), True)
	def testFind(self):
		t = BinaryTree.Tree()
		t.add(7)
		node = BinaryTree.Node(7)
		self.assertEqual(t.find(7).Value(), node.Value())


if __name__ == '__main__':
	unittest.main()
