'''
Problem:

Sort a list in less than n*log*n time, given the highest number in the list.


Thoughts:

We create a list of size n and use its indices to track the values of the original

list in sorted order. The values in the larger list represent the number of occurrences 

of that index in the list. Using the value in one array to index into another has my head 

spinning a little.


Source:

https://www.interviewcake.com/question/python/top-scores
'''

def sort_list(arr, max_val):
    all_possible_vals = [0] * (max_val + 1)
    sorted_list = []

    for val in arr:
        all_possible_vals[val] += 1

    for idx, val in enumerate(all_possible_vals):
        for i in range(val):
            sorted_list.append(idx)

    return sorted_list 

def main():
    MAXIMUM_VALUE = 100
    unsorted_list = [37, 89, 41, 65, 100, 91, 53, 41]
    sorted_list = sorted(unsorted_list)

    print sort_list(unsorted_list, MAXIMUM_VALUE) == sorted_list

if __name__ == '__main__':
    main()