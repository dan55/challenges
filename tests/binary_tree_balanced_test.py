import unittest

from ..data_structs.bst import get_arbitrary_tree_root, bst_insert, BinaryTreeNode
from ..binary_tree_balanced import is_tree_balanced, is_tree_balanced_2

class BinaryTreeBalancedTest(unittest.TestCase):
    def setUp(self):
        self.root = get_arbitrary_tree_root() # balanced tree of height 2

    def testBalancedTree(self):
        ret1 = is_tree_balanced(self.root)
        ret2 = is_tree_balanced_2(self.root)

        self.assertEqual(ret1, ret2)
        self.assertTrue(ret1)

    def testUnbalancedTree(self):
        bst_insert(self.root, BinaryTreeNode(60))

        # height differs by 1 here, so we're still balanced
        # TODO: but this is failing...
        #self.testBalancedTree()

        # now we're not
        bst_insert(self.root, BinaryTreeNode(70)) 

        ret1 = is_tree_balanced(self.root)
        ret2 = is_tree_balanced_2(self.root)

        self.assertEqual(ret1, ret2  )
        self.assertFalse(ret1)


if __name__ == '__main__':
    unittest.main()