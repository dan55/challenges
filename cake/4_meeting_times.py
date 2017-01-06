'''
Problem: 

Merge ranges of tuples. Like the room scheduling problem, but can sort on start time.


Thoughts:

Tuple unpacking is powerful.


Source:

https://www.interviewcake.com/question/python/merging-ranges
'''

import unittest

def merge_times(times):
    merged = []

    times = sorted(times)

    prev_start_time, prev_end_time = times.pop(0)

    for start_time, end_time in times:
        # we're safe to add the range
        # (i.e. we've found a result)
        if start_time > prev_end_time: 
            merged.append((prev_start_time, prev_end_time))

            prev_start_time = start_time
            prev_end_time = end_time
        else: 
            # preserve the earlier start time
            # the max handles the case in which an earlier
            # time completely 'subsumes' a later time
            prev_end_time = max(prev_end_time, end_time)

    # handle the final range, which must be safe to add
    merged.append((prev_start_time, prev_end_time))

    return merged

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
