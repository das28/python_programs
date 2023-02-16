def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

lst = [1,3,4,6,7,8,9]
total = sum_list(lst)
print(total)