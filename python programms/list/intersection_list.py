def intersection(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1,2,3,4,5]
list2 = [4,2,3,6,7]

print(intersection(list1,list2))