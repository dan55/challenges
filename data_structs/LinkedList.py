class LinkedListNode(object):

	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)

class LinkedList(object):

	def __init__(self, head=None):
		self.head = head

	def insert(self, node):
		if not self.head:
			self.head = node
			return self.head

		ptr = self.head

		# while there is another node
		while ptr.next:
			ptr = ptr.next

		# at last node
		ptr.next = node

		return self.head

	def delete(self, val_of_node_to_del):
		prev = None
		cur = self.head

		while cur and cur.value != val_of_node_to_del:
			prev = cur
			cur = cur.next 

		# not at end / found node to del
		if cur:
			if not prev: # at head of list
				self.head = cur.next
				cur.next = None
			#elif not cur.next # at last node
			#	prev.next = 
			else: 
				tmp = cur
				prev.next = cur.next

				tmp.next = None

	def __eq__(self, other):
		list(self) == list(other)

	def __iter__(self):
		ptr = self.head

		while ptr:
			yield ptr.value
			ptr = ptr.next

	def __str__(self):
		ret = ''
		ptr = self.head

		while ptr.next:
			ret += str(ptr.value) + ' -> ' 
			ptr = ptr.next

		ret += str(ptr.value)

		return ret

def _generate_test_list():
	_list = LinkedList()

	for i in range(1, 5):
		_list.insert(LinkedListNode(i))

	return _list

def get_head_of_arbitrary_list():
	return _generate_test_list().head

def get_arbitrary_linked_list():
	return _generate_test_list()