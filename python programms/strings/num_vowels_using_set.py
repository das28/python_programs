def num_vow(word):
    vowels = set("aeiouAEIOU")
    count = 0 
    for char in word:
        if char in vowels:
            count += 1
    return count

word = "you are a star"
print(num_vow(word))