def count_dig_lett(word):
    digit = 0
    letter = 0 
    for char in word:
        if char.isdigit():
            digit += 1
        else:
            letter += 1
    return (digit,letter)

word = "prara628pyeiemdsu32879"
print(count_dig_lett(word))