'''
Problem: 

Find the second largest element in a binary search tree.


Thoughts:

The second largest node can be either the parent of the rightmost / largest node 

OR the rightmost node in its left subtree. 


Source:

https://www.interviewcake.com/question/python/second-largest-item-in-bst
'''

def find_largest(root):
    curr = root

    while curr.right:
        curr = curr.right

    return curr

def find_second_largest(root):

    # second-largest may be parent of largest
    curr = root
    while curr.right and curr.right.right:
        curr = curr.right

    second_largest = curr
    
    
    # or it may be in the left subtree of largest
    largest = curr.right
    
    if largest.left:
        second_largest = find_largest(largest.left)

    return second_largest