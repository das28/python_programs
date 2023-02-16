def sum_nested_list(lst):
    total = 0
    for item in lst:
        if type(item) == list:
            total += sum_nested_list(item)
        else:
            total += item
    return total

lst = [1,2,3,[4,5],[5,6],[1,2]]
print(sum_nested_list(lst))