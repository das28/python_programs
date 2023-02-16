def check_key(dic,key):
    if key in dic:
        return True
    else:
        return False

d = {1:"a", 2:"b", 3:"c", 4:"d"}
key = 3
print(check_key(d,key))