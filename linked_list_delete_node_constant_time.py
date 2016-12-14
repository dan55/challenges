'''
Problem:

Given only a pointer to a node, delete the node in constant time.


Source:

https://www.interviewcake.com/question/python/delete-node
'''

from data_structs.LinkedList import *
import linked_list_delete_node

def delete_node(node):
    if not node.next:
        raise Exception('Cannot delete last node!')

    node.value = node.next.value
    node.next = node.next.next


def main():
    _linked_list = get_arbitrary_linked_list()
    head = _linked_list.head

    val_of_ptr_to_del = 1

    # Get the relevant node
    ptr = head
    node_to_del = None

    while ptr:
        if ptr.value == val_of_ptr_to_del:
            node_to_del = ptr
            break

        ptr = ptr.next

    # delete the node
    delete_node(node_to_del)

    # validate the method
    print list(_linked_list) == [2, 3, 4]

if __name__ == '__main__':
    main()

