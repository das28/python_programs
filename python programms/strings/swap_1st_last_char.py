def swap_letter(word):
    if len(word) > 1:
        return word[-1] + word[1:-1] + word[0]
    else:
        return word

word = "prarthana"
print(swap_letter(word))