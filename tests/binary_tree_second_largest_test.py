import unittest

from ..data_structs.bst import BinaryTreeNode, bst_insert, get_arbitrary_tree_root 
from ..bst_second_largest import find_largest, find_second_largest 

class BSTSecondLargestTester(unittest.TestCase): 
    def setUp(self):
        self.root = get_arbitrary_tree_root()

    def test_find_largest_helper(self):
        self.assertEqual(find_largest(self.root).val, 54)

    def test_second_largest_parent_of_largest(self):
        self.assertEqual(find_second_largest(self.root).val, 42) 

    def test_second_largest_in_left_subtree_of_largest(self):
        magic_num = 50

        bst_insert(self.root, BinaryTreeNode(magic_num))

        self.assertEqual(find_second_largest(self.root).val, magic_num) 


if __name__ == '__main__':
    unittest.main()