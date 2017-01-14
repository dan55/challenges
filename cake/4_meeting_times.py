'''
Problem: 

Merge ranges of tuples. Like the room scheduling problem, but can sort on start time.


Thoughts:

Tuple unpacking is powerful. And negative indexing.


Source:

https://www.interviewcake.com/question/python/merging-ranges
'''

import unittest

def merge_times(times):
    sorted_times = sorted(times)

    merged_times = [sorted_times[0]]

    for current_start_time, current_end_time in sorted_times[1:]:
        previous_start_time, previous_end_time = merged_times[-1]

        if current_start_time > previous_end_time: # no conflict
            merged_times.append((current_start_time, current_end_time))
        else:
            merged_times[-1] = ((previous_start_time, max(previous_end_time, current_end_time)))

    return merged_times

class UnitTest(unittest.TestCase):
    def test_that_the_func_works(self):
        times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        merged = [(0, 1), (3, 8), (9, 12)]
        
        self.assertEqual(merge_times(times), merged)

    def test_touching_times(self):
        times = [(1, 2), (2, 3)]
        merged = [(1, 3)]

        self.assertEqual(merge_times(times), merged)

    def test_subsumed_times(self):
        times = [(1, 5), (2, 3)]
        merged = [(1, 5)]

        self.assertEqual(merge_times(times), merged)

    def test_all_merged(self):
        times = [(1, 10), (2, 6), (3, 5), (7, 9)]
        merged = [(1, 10)]

        self.assertEqual(merge_times(times), merged)

if __name__ == '__main__':
    unittest.main()
    #print merge_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
