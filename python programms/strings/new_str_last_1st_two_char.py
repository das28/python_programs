def new_word(word):
    if len(word) < 2:
        return "Error: String lenght is less than 2."
    else:
        return word[0:2] + word[-2:]

word = "prarthana"
print(new_word(word))
