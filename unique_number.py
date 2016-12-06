'''
Problem:

Find the unique number in an array where all other numbers are pairs.

Can be done in theta(n) time.


Thoughts:

Any number xor'ed with itself is 0. Any number xor'ed with 0 is that number.

Thus, we walk through the list, and all of the pairs cancel to 0, leaving

the number we're searching for.


Can be used when 'you want to "cancel out" matching numbers'


Sources:

https://www.interviewcake.com/question/python/find-unique-int-among-duplicates

https://www.hackerrank.com/challenges/ctci-lonely-integer
'''

def get_unique_num(arr):
    target = 0

    for num in arr:
        target ^= num

    return target

print(get_unique_num([8, 34, 12, 12, 8]) == 34) 