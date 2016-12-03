'''
Determine the largest number that can be formed from a list of non-negative integers.

A Java solution is presented here:

http://www.programcreek.com/2014/02/leetcode-largest-number-java/

The central idea, I think, is to do a sort in which the comparison is based on the concatentation of the integers.

For example, if we have 3 and 30, we chose 3 + 30 = 330 rather than 30 + 3 = 303. 
'''

def largest_number(a):
	a_as_str = map(str, a)

	a_sorted = sorted(a_as_str, cmp=lambda x, y: cmp(x + y, y + x), reverse=True)

	return ''.join(a_sorted)

'''
We could do this in one line if we wanted it to be incomprehensible.
'''

largest_num_lambda = lambda x: ''.join(sorted(map(str, x), cmp=lambda x,y: cmp(x + y, y + x), reverse=True))

example = [3, 30, 34, 5, 9]
answer = '9534330'

print(largest_number(example) == largest_num_lambda(example) == answer)