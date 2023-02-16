def count_lower(word):
    count = 0 
    for char in word:
        if char.islower():
            count += 1
    return count

word = "Prarthana"
print(count_lower(word))