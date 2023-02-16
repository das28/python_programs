def remove_key(d,key):
    if key in d:
        del d[key]
    return d

d =  {'a': 1, 'b': 2, 'c': 3}
print(remove_key(d,"b"))