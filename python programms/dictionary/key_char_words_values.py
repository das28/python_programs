words = ['apple','banana', 'dog','cat', 'elephant']

result = {}
for word in words:
    if word[0] not in result:
        result[word[0]] = [word]
    else:
        result[word[0]].append(word)
print(result)