'''
The classic. For integers between 1 and 100, inclusive:

	1) If the number is divisible by 3, print "Fizz"
	
	2) If the number is divisible by 5, print "Buzz"
	
	3) If the number is divisible by both 3 and 5, print "FizzBuzz"

What could go wrong? Well, among other things:

	1) Given the structure of the question, you test whether the integer is 
	divisible by 3 AND 5 AFTER checking whether it is divisible by 3 OR 5.
	The former condition is never hit, FizzBuzz is never printed, and your
	interview is off to a bad start.

	2) You forget how modulo works, because some operators just don't come up everyday.
	Under stress, I sometimes think that modulo actually means divisible by and forget
	to check that the remainder equals 0. This is especially unfortunate in languages for 
	which non-zero integers are truthy.
'''

def fizz_buzz(n):
	if n % 3 == 0and n % 5 == 0:
		return "FizzBuzz"
	elif n % 3 == 0:
		return "Fizz"
	elif n % 5 == 0:
		return "Buzz"
	else:
		return n


'''
Perhaps it would be useful to write a helper function for cleanliness and to remind yourself
of the operation you're actually trying to perform.
'''

def is_divisible_by(n, divisor):
	return n % divisor == 0

def fizz_buzz_decomposed(n):
	if is_divisible_by(n, 3) and is_divisible_by(n, 5):
		return "FizzBuzz"
	elif is_divisible_by(n, 3):
		return "Fizz"
	elif is_divisible_by(n, 5):
		return "Buzz"
	else:
		return n


'''
Inspiration from: http://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail/
'''

def fizz_buzz_improved(n):
	fizz = lambda x: is_divisible_by(x, 3)
	buzz = lambda x: is_divisible_by(x, 5)

	if fizz(n) and buzz(n):
		return "FizzBuzz"
	elif fizz(n):
		return "Fizz"
	elif buzz(n):
		return "Buzz"
	else:
		return n


def main():
	n = 100

	ret_from_fizz_buzz = [fizz_buzz(i) for i in range(1, n + 1)]
	ret_from_fizz_buzz_decomposed = [fizz_buzz_decomposed(i) for i in range(1, n + 1)]
	ret_from_fizz_buzz_improved = [fizz_buzz_improved(i) for i in range(1, n + 1)]

	print(ret_from_fizz_buzz == ret_from_fizz_buzz_decomposed == ret_from_fizz_buzz_improved)
	
	for i in ret_from_fizz_buzz:
		print i

if __name__ == '__main__':
	main()
