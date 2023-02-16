def not_str(word1,word2):
    res = []
    for char in word1:
        if char not in word2:
            res.append(char)
    return (res)

word1 = "prarthana"
word2 = "puneet"

print(not_str(word1,word2))