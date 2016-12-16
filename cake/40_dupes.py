'''
Problem:

Find the duplicate number in a list in constant space, n(log(n)) time

and without altering the list.


Thoughts:

Imagine the array were sorted. By determining how many of the elements

are greater than the midpoint, we know in which direction to look next.

It turns out we can do the same operation on an unsorted array, and it 

still works, somehow.


Source:

https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space
'''


def find_repeat(arr):

    floor = 1
    ceiling = len(arr) - 1

    while floor < ceiling:

        midpoint = (ceiling - floor) / 2

        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling

        elems_in_lower_range = 0

        for elem in arr:
            if elem >= lower_range_floor and elem <= lower_range_ceiling:
                elems_in_lower_range += 1

        number_of_possible_distinct_ints_in_lower_range = \
            lower_range_ceiling - lower_range_floor + 1

        if elems_in_lower_range > number_of_possible_distinct_ints_in_lower_range:
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            floor, ceiling = upper_range_floor, upper_range_ceiling

    return arr[floor] 


def main():

    print find_repeat([4, 1, 4, 2]) == 4
    print find_repeat([1, 1, 4, 3]) == 1



if __name__ == '__main__':
    main()