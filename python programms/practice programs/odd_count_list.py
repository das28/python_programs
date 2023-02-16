def odd_occ(lst):
    result = 0
    for i in lst:
        result = result ^ i
    return result

lst = [1,2,3,5,3,2,4,6,4,7,8,4,2]  
print(odd_occ(lst))