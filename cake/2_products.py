'''
Problem: 

Given a list of numbers, generate a list of the products of all the numbers 

except that at the index. Makes perfect sense, right?


Thoughts: 

The product of all of the numbers except the number at the index is 

the product of all the numbers before the index times all the numbers after the index. 


I am finding even the brute force method to be worth writing...for practice...


Source: 

https://www.interviewcake.com/question/python/product-of-other-numbers

'''
import unittest

def product_of_all_but_idx(arr):
    len_of_arr = len(arr)

    prods = [None] * len_of_arr

    # generate all the products before the index
    prod_so_far = 1

    for idx in range(len_of_arr):
        prods[idx] = prod_so_far
        prod_so_far *= arr[idx]


    # generate all the products after the index
    prod_so_far = 1
    idx = len_of_arr - 1
    
    while idx >= 0:
        prods[idx] *= prod_so_far
        prod_so_far *= arr[idx]
        idx -= 1

    return prods

def brute_force(arr):
    prods = []

    for idx in range(len(arr)):
        
        prod_so_far = 1

        for idx_inner, num in enumerate(arr):
        
            if idx_inner == idx:
                continue

            prod_so_far *= num

        prods.append(prod_so_far)

    return prods

class TestCase(unittest.TestCase):
    def test_if_this_works(self):
        arr = [1, 7, 3, 4]
        ans = [84, 12, 28, 21]

        self.assertEqual(product_of_all_but_idx(arr), ans)
        self.assertEqual(product_of_all_but_idx(arr), brute_force(arr))

if __name__ == '__main__':
    unittest.main()