class LinkedListNode(object):

	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)

class LinkedList(object):

	def __init__(self, head):
		self.head = head

	def insert(self, node):
		ptr = self.head

		# while there is another node
		while ptr.next:
			ptr = ptr.next

		# at last node
		ptr.next = node

	def __str__(self):
		ret = ''
		ptr = self.head

		while ptr.next:
			ret += str(ptr.value) + ' -> ' 
			ptr = ptr.next

		ret += str(ptr.value)

		return ret
