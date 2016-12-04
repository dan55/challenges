'''
Problem: Determine whether a binary tree is balanced. A tree is balanced if the 

height of left and right subtrees differ by no more than 1.
'''

def get_tree_height(root):
    if root is None:
        return 0

    return max(get_tree_height(root.left), get_tree_height(root.right)) + 1

def is_tree_balanced(root):
    if root is None:
        return True

    left_height = get_tree_height(root.left)
    right_height = get_tree_height(root.right)

    if abs(left_height - right_height) > 1:
        return False
    else:
        return is_tree_balanced(root.left) and is_tree_balanced(root.right)

'''
More cleanly...
'''

def is_tree_balanced_2(root):
    if root is None:
        return True # we've explored all subtrees

    return abs(get_tree_height(root.left) - get_tree_height(root.right)) <= 1 \
        and is_tree_balanced_2(root.left) and is_tree_balanced_2(root.right)