'''
Problem:

Reverse a linked list. Can be trickier than you'd imagine.


Thoughts:

Remember to initialize previous_node to None to avoid confusion and then panic.


Source:

https://www.interviewcake.com/question/python/reverse-linked-list

https://www.hackerrank.com/challenges/reverse-a-linked-list
'''

from data_structs import LinkedList 

def reverse_list(head):
    current_node = head
    previous_node = None

    while current_node:
        # store the pointer to the next node 
        # before reversing the node's pointer
        next_node = current_node.next

        # reverse the node's pointer
        current_node.next = previous_node

        # move forward
        previous_node = current_node
        current_node = next_node

    return previous_node