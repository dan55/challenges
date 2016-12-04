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


vals = [i for i in range(1, 4)]

linked_list_head = LinkedList.LinkedListNode(vals.pop(0))
linked_list = LinkedList.LinkedList(linked_list_head)

print(linked_list_head)

for val in vals:
    linked_list.insert(LinkedList.LinkedListNode(val))

print(linked_list)
import pdb; pdb.set_trace()
linked_list.head = reverse_list(linked_list_head)

print(linked_list)