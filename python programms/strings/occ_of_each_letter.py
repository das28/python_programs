def word_count(word):
    words = word.split()
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

word= 'the dog sudden jumped on the fox'
print(word_count(word))