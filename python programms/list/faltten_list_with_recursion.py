def flatten_list(lst):
    flat_list = []
    for i in lst:
        if type(i) == list:
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)

    return flat_list

lst = [1, [2, [3, 4], [5, 6]], 7, [8, 9]]
print(flatten_list(lst))