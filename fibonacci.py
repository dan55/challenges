'''
Sources:

https://www.interviewcake.com/question/python/nth-fibonacci
'''

import itertools 


def iterative():
	a, b = 1, 1

	while True:
		yield a

		a, b = b, a + b


def recursive(n):
	if n < 2:
		return n 

	return recursive(n - 1) + recursive(n - 2)


def memoized(n, cache={}):
	if n < 2:
		return n

	if n in cache:
		return cache[n]

	cache[n] = memoized(n - 1) + memoized(n - 2)

	return cache[n]


def main():
	n = 30

	print(list(itertools.islice(iterative(), n)).pop() == recursive(n) == memoized(n))

if __name__ == '__main__':
	main()
