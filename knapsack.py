'''
Problem: 

Given the weights and values of a set of items and the capacity of a knapsack,

find the combination of items that will maximize the value of the knapsack.


Source:

https://www.interviewcake.com/question/python/cake-thief
'''


from collections import namedtuple

def get_max_val(items, capacity, cur_idx=None):
    # set idx in initial call only
    if cur_idx is None:
        cur_idx = len(items) - 1

    # base case: we've run out of items
    if cur_idx < 0:
        return 0

    # get the weight and value of the current item
    cur_item = items[cur_idx]
    cur_weight, cur_val = cur_item.weight, cur_item.value

    # if the current weight exceeds capacity,
    # move to the next item
    if capacity - cur_weight < 0:
        return get_max_val(items, capacity, cur_idx - 1) 

    # recursively determine the maximum values obtained 
    # both from using and not using the current item
    max_with_item = cur_val + get_max_val(items, capacity - cur_weight, cur_idx - 1)
    max_without_item = get_max_val(items, capacity, cur_idx - 1)

    # choose whichever of those options yields the higher value
    return max(max_with_item, max_without_item)




def main():
    Item = namedtuple('Item', ['weight', 'value'])
    unnamed_items = [(7, 160), (3, 90), (2, 15)]
    named_items = []

    for item in unnamed_items:
        named_items.append(Item(item[0], item[1])) 

    capacity = 20
    max_val = 265

    print get_max_val(named_items, capacity) == max_val


if __name__ == '__main__':
    main()