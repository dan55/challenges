import unittest

from ..data_structs.LinkedList import LinkedList, LinkedListNode
from ..linked_list_delete_node import delete_node

class LinkedListDeleteNodeTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

        for i in range(3):
            self.linked_list.insert(LinkedListNode(i))

        self.test_deleted_middle = [0, 2]
        self.test_deleted_end = [0, 1]
        self.test_deleted_head = [1, 2]

    def test_delete_middle_node(self):
        delete_node(self.linked_list.head, 1)

        self.assertEqual(list(self.linked_list), self.test_deleted_middle)

    def test_delete_last_node(self):
        delete_node(self.linked_list.head, 2)

        self.assertEqual(list(self.linked_list), self.test_deleted_end)

    def test_delete_first_node(self):
        new_list_head = delete_node(self.linked_list.head, 0)

        self.assertEqual(list(self.linked_list), self.test_deleted_head)

class LinkedListMemberDeleteTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

        for i in range(3):
            self.linked_list.insert(LinkedListNode(i))

        self.test_deleted_middle = [0, 2]
        self.test_deleted_end = [0, 1]
        self.test_deleted_head = [1, 2]

    def test_delete_middle_node(self):
        self.linked_list.delete(1)

        self.assertEqual(list(self.linked_list), self.test_deleted_middle)

    def test_delete_last_node(self):
        self.linked_list.delete(2)

        self.assertEqual(list(self.linked_list), self.test_deleted_end)

    def test_delete_first_node(self):
        self.linked_list.delete(0)

        self.assertEqual(list(self.linked_list), self.test_deleted_head)

if __name__ == '__main__':
    unittest.main()