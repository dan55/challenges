'''

Write a function that returns True if a linked list contains a cycle and False otherwise.

We use two pointers that traverse the list at different speeds. Imagine yourself and Usain Bolt
running on a track. If the track is circular, he will overlap you.

Interview Cake has a nice proof that the faster pointer cannot "skip over" the slow pointer. 
They must at some iteration point to the same node.

Sources:

https://www.interviewcake.com/question/python/linked-list-cycles

https://www.hackerrank.com/challenges/ctci-linked-list-cycle

'''

class Node(object):

	def __init__(self, val):
		self.val = val
		self.next = None


def has_cycle(head):
	fast_ptr = head
	slow_ptr = head

	while fast_ptr and fast_ptr.next:
		slow_ptr = slow_ptr.next
		fast_ptr = fast_ptr.next.next

		if slow_ptr == fast_ptr:
			return True
	
	return False

def main():
	head = Node(1)
	ptr = head

	for i in range(2, 10):
		ptr.next = Node(i)
		ptr = ptr.next

	print(has_cycle(head))

	ptr.next = head

	print(has_cycle(head))

if __name__ == '__main__':
	main()