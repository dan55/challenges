'''
Problem:

Determine whether a binary tree is a binary search tree.


Thoughts:

If we go left, we better not encounter anything larger than what we just encountered, and vice versa.


Sources:

https://www.interviewcake.com/question/python/bst-checker

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
'''
import unittest

from helpers import bst

def is_valid_bst(root, lower_bound=float('-inf'), upper_bound=float('inf')):

	if not root:
		return True

	val, left, right = root.val, root.left, root.right

	if val < lower_bound or val > upper_bound:
		return False

	return is_valid_bst(left, lower_bound, val) and is_valid_bst(right, val, upper_bound)


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

