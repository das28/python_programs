def sort_2nd(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_2nd([[1, 4], [3, 2], [2, 1]]))
