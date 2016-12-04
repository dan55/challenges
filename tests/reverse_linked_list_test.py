import unittest 

from ..data_structs.LinkedList import LinkedListNode, LinkedList
from ..linked_list_reverse import reverse_list

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        vals = [i for i in range(1, 4)]
        self.linked_list = self.constructList(vals)
        vals.reverse()
        self.linked_list_reversed = self.constructList([3,2,1])

    def constructList(self, vals):
        # TODO: can we instantiate a list from an array in the class?

        linked_list_head = LinkedListNode(vals.pop(0))
        linked_list = LinkedList(linked_list_head)

        for val in vals:
            linked_list.insert(LinkedListNode(val))

        return linked_list

    def testReverse(self):
        reversed = [] 

        ptr = reverse_list(self.linked_list.head)

        while ptr:
            reversed.append(ptr.value)
            ptr = ptr.next

        self.assertEqual(reversed, list(self.linked_list_reversed))

    def testReverseOnEmptyList(self):
        self.assertEqual(reverse_list(None), None)

    def testReverseOnListWithOneNode(self):
        node = LinkedListNode(1)
        linked_list = LinkedList(node)

        self.assertEqual(node, reverse_list(linked_list.head))

if __name__ == '__main__':
    unittest.main()