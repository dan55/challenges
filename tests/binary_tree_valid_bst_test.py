import unittest

from ..binary_tree_valid_search_tree import is_valid_bst
from ..data_structs import bst


class ValidBSTChecker(unittest.TestCase):
    
    def setUp(self):
        self.root = bst.BinaryTreeNode(50)

        for val in [30, 80, 20, 70, 90]:
            bst.bst_insert(self.root, bst.BinaryTreeNode(val))

    def test_validity_checker_for_valid_bst(self):
        self.assertTrue(is_valid_bst(self.root))

    def test_validity_checker_for_invalid_bst(self):
        # the example from interview cake
        self.root.left.right = bst.BinaryTreeNode(60)

        self.assertFalse(is_valid_bst(self.root))

if __name__ == '__main__':
    unittest.main()
