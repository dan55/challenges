'''
Problem:

Determine whether a binary tree is a binary search tree.


Thoughts:

If we go left, we better not encounter anything larger than what we just encountered, 

so we have a new upper bound. If we are in a right subtree, we should not find any smaller

values, so we have a new lower bound.


Sources:

https://www.interviewcake.com/question/python/bst-checker

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
'''
import unittest

from data_structs import bst

def is_valid_bst(root, lower_bound=float('-inf'), upper_bound=float('inf')):

	if not root:
		return True

	val, left, right = root.val, root.left, root.right

	if val < lower_bound or val > upper_bound:
		return False

	return is_valid_bst(left, lower_bound, val) and is_valid_bst(right, val, upper_bound)