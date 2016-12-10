def get_max_val(weights, values, capacity, cur_idx):
    if cur_idx < 0:
        return 0

    if capacity - weights[cur_idx] < 0:
        return get_max_val(weights, values, capacity, cur_idx - 1) 

    max_with_item = values[cur_idx] + get_max_val(weights, values, capacity - weights[cur_idx], cur_idx - 1)
    max_without_item = get_max_val(weights, values, capacity, cur_idx - 1)

    return max(max_with_item, max_without_item)


[(7, 160), (3, 90), (2, 15)]
capacity    = 20

weights = [2, 3, 7]
values = [15, 90, 160]

print get_max_val(weights, values, capacity, len(weights) - 1)