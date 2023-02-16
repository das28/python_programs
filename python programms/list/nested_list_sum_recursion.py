def nested_list_sum(lst):
    total = 0 
    for i in lst:
        if type(i) == list:
            total += nested_list_sum(i)
        else:
            total += i
    return total

lst = [1, 2, [3, 4, [5, 6]]]
print(nested_list_sum(lst))