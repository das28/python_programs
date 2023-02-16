def remove_word(lst, word, i):
    count = 0 
    index = 0
    for ele in lst:
        if ele == word:
            count += 1
            if count == i:
                index = lst.index(ele)
                break
    lst.pop(index)
    return(lst)

print(remove_word(["apple", "banana", "cherry", "apple"], "apple", 2))    
