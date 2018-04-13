import unittest
import LinkedList

class LinkedListTest(unittest.TestCase):
	def testSize(self):
		l = LinkedList.LinkedList()
		l.Insert(1)
		l.Insert(2)
		self.assertEqual(l.Size(), 2)
	def testSearch(self):
		l = LinkedList.LinkedList()
		l.Insert(1)
		l.Insert(2)
		self.assertEqual(l.Search(9), None)
		self.assertEqual(l.Search(2).value, 2)
	def testDelete(self):
		l = LinkedList.LinkedList()
		l.Insert(1)
		l.Insert(2)
		self.assertEqual(l.Search(2).value, 2)
		l.Delete(1)
		self.assertEqual(l.Search(1), None)
		self.assertEqual(l.Size(), 1)

if __name__ == '__main__':
	unittest.main()
