def count_both(word):
    lower = 0 
    upper = 0
    for char in word:
        if char.islower():
            lower += 1
        else:
            upper += 1
    return(lower,upper)

word = "PrartHANA"
print(count_both(word))