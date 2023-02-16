def flatten(lst):
    flat_list = []
    for i in lst:
        if type(i) == list:
            flat_list.extend(flatten(i))
        else:
            flat_list.append(i)
    return flat_list

lst = [1, [2, [3, 4], 5]]
print(flatten(lst))