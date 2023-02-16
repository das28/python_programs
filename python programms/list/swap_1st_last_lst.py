def swap(lst):
    if len(lst) < 2:
        return lst
    lst[0],lst[-1] = lst[-1],lst[0]
    return lst

print(swap([1,3,4,5,6,7,8]))