'''


To determine the number of ways to make 5c, we record the number of ways to make 

1c, 2c, 3c, 4c, 5c from 1c

3c, 4c, 5c from 3c or 1c

5c from 5c or 3c or 1c


We know we can always make remainder cents from the current denom.

And we know how many ways we can make remainder cents from previous denoms.

Or something.

Look at the tabulation provided by Inteview Cake, but ADD THE ARRAY INDICES!


'''

def find_num_ways_to_make_change(amount, denoms):
    
    # We'll record every way to make change from 0 to amount
    num_ways = [0] * (amount + 1)
    num_ways[0] = 1

    for denom in denoms:
        for higher_amount in range(denom, amount + 1):
            remainder = higher_amount - denom
            num_ways[higher_amount] += num_ways[remainder]

    return num_ways[amount]


def main():
    amt = 5
    denoms = [1, 3, 5]
    import pdb; pdb.set_trace()
    print find_num_ways_to_make_change(amt, denoms)

if __name__ == '__main__':
    main()