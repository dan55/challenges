'''
Problem:

Find how many ways can we make n cents from arbitrary denominations.


Thoughts:

It is known that once you wrap your head around dynamic programming, it's 

not complicated, which means I have not wrapped my head around it. The below

code strikes me as very subtle and tricky, as well as elegant.


Source:

https://www.interviewcake.com/question/python/coin
'''


'''
Bottom-up approach:


For each denomination, we literally tabulate the number of ways we can make each

amount of change from the smallest denomination to n. 


Note the importance of the initialization of num_ways_to_make_i_cents[0], 

which is the building block for everything that follows. The intuition is 

that there is one way to make 0 cents, namely, 0 cents, or something. 

The importance, though, is that anytime we make an even amount of change (0 cents), 

we need to add 1 to the total number of ways we've found of making n cents. 


The final code box at Interview Cake is a useful visualization, if you add the indices 

to the arrays.
'''

def get_number_ways_to_make_n_cents(n, denoms):
    num_ways_to_make_i_cents = [0] * (n + 1)
    num_ways_to_make_i_cents[0] = 1

    for denom in denoms:
        for inc_amt in range(denom, n + 1):
            remaining = inc_amt - denom
            num_ways_to_make_i_cents[inc_amt] += num_ways_to_make_i_cents[remaining]

    return num_ways_to_make_i_cents[n]


'''
Top-down approach:


Note the following:


1) The order of the returns. If the last denomination in the list makes

even change, we must return 1, though the index has exceeded the length 

of the list at this call. This check must come first.


2) The recursive all contains a while loop in which we're iteratively 

cutting down amount. At the same time, we're increasing the index, 

progressing through the denominations. Hence, the base cases, and 

your head spinning. 
'''

def get_number_ways_to_make_n_cents_recursively(amt, denoms, cur_idx=0):
   
    # found 1 way to make amt 
    if amt == 0:
        return 1

    # base cases
    if amt < 0 or cur_idx == len(denoms):
        return 0

    num_ways_to_make_n_cents = 0
    cur_denom = denoms[cur_idx]

    while amt >= 0:
        num_ways_to_make_n_cents += get_number_ways_to_make_n_cents_recursively(amt, denoms, cur_idx + 1)

        amt -= cur_denom

    return num_ways_to_make_n_cents

def main():
    amt = 5
    denoms = [1, 3, 5]

    print \
        get_number_ways_to_make_n_cents(amt, denoms) \
        == get_number_ways_to_make_n_cents_recursively(amt, denoms) \
        == 3

if __name__ == '__main__':
    main()