'''
Problem:

Determine whether a binary tree is a binary search tree.


Sources:

https://www.interviewcake.com/question/python/bst-checker

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
'''

def is_valid_bst(head, lower_bound=float('-inf'), upper_bound=float('inf')):

	left = head.left
	right = head.right

	if left:
		if left.val > lower_bound:
			return False

		is_valid_bst(left, left.val, upper_bound)

	if head.right:
		if right.val < upper_bound:
			return False

		is_valid_bst(right, lower_bound, right.val)

	return True
