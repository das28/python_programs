def union(list1,list2):
    return list(set(list1) | set(list2))

list1 = [1,2,3,4]
list2 = [4,5,3,2]

print(union(list1,list2))