import unittest

from ..queue_from_stacks import Queue

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.test_vals = [i for i in range(5)]

    def test_this_more_or_less_works(self):
        for val in self.test_vals:
            self.q.enqueue(val)

        self.assertEqual(self.q.dequeue(), self.test_vals.pop(0))
        self.assertEqual(self.q.dequeue(), self.test_vals.pop(0))

        self.q.enqueue(6)

        remaining = []

        for i in range(len(self.test_vals)):
            remaining.append(self.q.dequeue())

        self.assertEqual(remaining, self.test_vals)

        self.assertEqual(self.q.dequeue(), 6)

if __name__ == '__main__':
    unittest.main()