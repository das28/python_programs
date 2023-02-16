def count_vow(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = "pikachu"
print(count_vow(word))
        