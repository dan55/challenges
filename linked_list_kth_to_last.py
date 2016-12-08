'''
Problem: 

Get the kth to last node in a singly-linked list


Thoughts:

First instinct was to use a stack, which would save one traversal but is O(n)

space. Two traversals is still O(n) time and requires far less space (a ptr and a function call).


Source:

https://www.interviewcake.com/question/python/kth-to-last-node-in-singly-linked-list
'''
from data_structs.LinkedList import get_head_of_arbitrary_list

def get_list_length(head):
    nodes = 1
    cur = head

    while cur:
        cur = cur.next
        nodes += 1 

    return nodes

def get_kth_to_last_node(k, head):
    nodes = get_list_length(head)

    cur = head
    num_steps = nodes - k

    while num_steps:
        cur = cur.next
        num_steps -= 1

    return cur



def main():
    head = get_head_of_arbitrary_list()
    
    print get_kth_to_last_node(2, head).value == 4
    print get_kth_to_last_node(5, head).value == 1


if __name__ == '__main__':
    main()