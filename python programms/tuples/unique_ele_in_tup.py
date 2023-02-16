val = [(1, 3, 5), (4, 5, 7), (1, 2, 6), (10, 9), (10,)]
result = set()
for tup in val:
    for item in tup:
        result.add(item)
print(list(result))