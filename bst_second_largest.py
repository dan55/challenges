'''
Problem: 

Find the second largest element in a binary search tree.


Thoughts:

First notice that the second largest node can be either the parent of the rightmost (max) node 

OR the rightmost node in the left subtree of that node. Is that a sentence? 


In any case, it's probably also worth introducing the third pointer to handle the latter check

and leaving one dangling at the max node, or else you may find yourself kicking yourself during

the return, depending on whether a left subtree exists or not.


Source:

https://www.interviewcake.com/question/python/second-largest-item-in-bst
'''

def find_second_largest(root):
    cur = root
    parent_of_max = None
    left_subtree_of_max_ptr = None

    while cur.right:
        parent_of_max = cur
        cur = cur.right

    if cur.left:
        left_subtree_of_max_ptr = cur.left

        while left_subtree_of_max_ptr.right:
            left_subtree_of_max_ptr = left_subtree_of_max_ptr.right

    if left_subtree_of_max_ptr and left_subtree_of_max_ptr.val > parent_of_max.val:
        return left_subtree_of_max_ptr
    else:
        return parent_of_max


def main():
    from data_structs.bst import get_arbitrary_tree_root, BinaryTreeNode, bst_insert

    root = get_arbitrary_tree_root()

    print find_second_largest(root).val == 42

    # second largest is now max node's left child
    new_node = BinaryTreeNode(50)
    bst_insert(root, new_node)

    print find_second_largest(root) == new_node

    # second largest is now to the right of max node's left child
    new_node = BinaryTreeNode(52)
    bst_insert(root, new_node)
    
    print find_second_largest(root) == new_node

if __name__ == '__main__':
    main()