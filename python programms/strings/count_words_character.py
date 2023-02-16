def count_wc(str):
    word = str.split()
    word_count = len(word)
    len_char = len(str)
    return word_count, len_char

str = "prarthana das"
print(count_wc(str))