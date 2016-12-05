'''
Thoughts: Useful to do some walking through lists if you're rusty.
'''


# Brute force: for every price, compare all later prices

def get_max_profit(prices):
    max_profit = None

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit

# "greedy"

def get_max_profit_greedy(prices):
    min_so_far = prices.pop(0)
    max_profit = None

    for price in prices:
        min_so_far = min(min_so_far, price)
        max_profit = max(max_profit, price - min_so_far)

    return max_profit


prices = [10, 7, 5, 8, 11, 9]
print get_max_profit(prices)
print get_max_profit_greedy(prices)


# Note this does not account for edge cases:
# 1) Decreasing prices
# 2) Insufficient number of prices

prices = [10, 5, 2]
print get_max_profit(prices)
print get_max_profit_greedy(prices)