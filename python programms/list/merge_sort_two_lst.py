def merge_sort(list_1, list_2):
    merge_list = list_1 + list_2
    return sorted(merge_list)

print(merge_sort([1,2,3],[4,5,6]))