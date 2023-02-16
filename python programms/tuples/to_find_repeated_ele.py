def find_repeated(tup):
    d = {}
    repeated = []
    for i in tup:
        if i in d:
            repeated.append(i)
        else:
            d[i] = 1
    return repeated

tup = (1, 2, 3, 4, 1, 2, 3)
print(find_repeated(tup))