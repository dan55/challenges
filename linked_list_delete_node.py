def delete_node(head, val_of_node_to_del):
    cur = head
    prev = None

    while cur:
        if cur.value == val_of_node_to_del:
            if cur.next:
                if prev:
                    cur = cur.next
                    tmp = prev.next
                    prev.next = cur

                    prev = tmp
                    prev.next = None

                    prev = cur
                else: # we're at the head of the list
                    tmp = cur.next
                    cur.next = None
                    cur = tmp

                    return cur
            else: # we're at the end of the list
                prev.next = None

            return head

        prev = cur
        cur = cur.next