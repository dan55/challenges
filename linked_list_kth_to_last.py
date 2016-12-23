'''
Problem: 

Get the kth to last node in a singly-linked list


Thoughts:

First instinct was to use a stack, which would save one traversal but is O(n)

space. Two traversals is still O(n) time and requires far less space (a ptr and a function call).

Alternatively, we can use a trailing pointer spaced k steps before the head pointer, but note

that this is still the same number of instructions as two traversals...


Source:

https://www.interviewcake.com/question/python/kth-to-last-node-in-singly-linked-list
'''
from data_structs.LinkedList import get_arbitrary_linked_list

def get_list_length(head):
    nodes = 0
    cur = head

    while cur:
        nodes += 1 
        cur = cur.next

    return nodes

def get_kth_to_last_node(k, head):
    num_nodes = get_list_length(head)

    # It takes n - 1 steps to get to the end
    # of a list of length n
    num_steps_to_take = num_nodes - k - 1

    cur = head

    while num_steps_to_take:
        cur = cur.next
        num_steps_to_take -= 1

    return cur


def get_kth_to_last_node_alt(k, head):
    curr = head
    k_behind = head

    for _ in range(k):
        curr = curr.next

    while curr.next:
        curr = curr.next
        k_behind = k_behind.next    

    return k_behind

def main():
    linked_list = get_arbitrary_linked_list()

    print get_kth_to_last_node(0, linked_list.head).value == get_kth_to_last_node_alt(0, linked_list.head).value == 4
    print get_kth_to_last_node(2, linked_list.head).value == get_kth_to_last_node_alt(2, linked_list.head).value == 2
    print get_kth_to_last_node(3, linked_list.head).value == get_kth_to_last_node_alt(3, linked_list.head).value == 1

if __name__ == '__main__':
    main()