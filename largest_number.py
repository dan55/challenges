'''
Problem: 

Determine the largest number that can be formed from a list of non-negative integers.


Thoughts:

We treat the numbers as strings, sort them, and concatenate them. But how do we sort them? By concatenating them.

For example, if we have 3 and 30, we place 3 + 30 = 330 before 30 + 3 = 303. 

I can't fully wrap my mind around this.


Sources:

http://www.programcreek.com/2014/02/leetcode-largest-number-java/
'''

def concat_sort(str1, str2):
	str1_then_str2 = str1 + str2
	str2_then_str1 = str2 + str1

	if str1_then_str2 > str2_then_str1:
		return 1
	elif str2_then_str1 > str1_then_str2:
		return -1 

	return 0

def largest_number(a):
	a_as_str = map(str, a)

	a_sorted = sorted(a_as_str, cmp=concat_sort, reverse=True)

	return ''.join(a_sorted)


'''
We can just use the built-in cmp function. 
'''

def largest_number_cmp(a):
	a_as_str = map(str, a)

	a_sorted = sorted(a_as_str, cmp=lambda x,y: cmp(x + y, y + x), reverse=True)

	return ''.join(a_sorted)


'''
We could even do this in one line. The only difficulty is that it is incomprehensible.
'''

largest_num_lambda = lambda x: ''.join(sorted(map(str, x), cmp=lambda x,y: cmp(x + y, y + x), reverse=True))


def main():
	example = [3, 30, 34, 5, 9]
	answer = '9534330'

	print(largest_number(example) == largest_number_cmp(example) == largest_num_lambda(example) == answer)


if __name__ == '__main__':
	main()