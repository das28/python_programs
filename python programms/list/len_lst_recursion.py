def list_len(lst):
    if not lst:
        return 0 
    else:
        return 1 + list_len(lst[1:])

print(list_len([1,2,3,4,5,6,7]))
