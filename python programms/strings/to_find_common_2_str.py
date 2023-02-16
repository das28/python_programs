def comman_both(str1, str2):
    common = []
    for char in str1:
        if char in str2:
            common.append(char)
    return common

str1 = "pr"
str2 = "prarthana"
print(comman_both(str1,str2))