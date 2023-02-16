def rev_str(word):
    rev_word = ""
    for char in word:
        rev_word = char + rev_word
    return rev_word

word = "chiku"
print(rev_str(word))