from linklist import *
import unittest

class TestsLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list2 = LinkedList()

    def test_append(self):
        self.assertEqual(self.linked_list.append(3), True)
        self.assertEqual(self.linked_list2.append(4), True)

    def test_get_index(self):
        self.linked_list.append(5)
        self.linked_list.append(7)
        self.linked_list.append(2)
        self.assertEqual(self.linked_list.get_index(2), -1)
        self.assertEqual(self.linked_list2.get_index(2), -1)

if __name__ == '__main__':
    unittest.main()