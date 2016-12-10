class BinaryTreeNode(object):

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __eq__(self, other):
		return self.val == other.val

	def __lt__(self, other):
		return self.val < other.val

	def __repr__(self):
		return str(self.val)

	def __str__(self):
		return str(self.val)

def bst_insert(root, node):
	if node < root:
		if root.left:
			bst_insert(root.left, node)
		else:
			root.left = node
	else:
		if root.right:
			bst_insert(root.right, node)
		else:
			root.right = node

def inorder(root):
	if not root:
		return

	inorder(root.left)
	print(root)
	inorder(root.right)

def get_arbitrary_tree_root():
	vals = [24, 42, 12, 15, 54]

	root = BinaryTreeNode(vals.pop(0))

	for val in vals:
		bst_insert(root, BinaryTreeNode(val))

	return root