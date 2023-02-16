def long_word(word_list):
    res=max(word_list,key=len)
    return (res,len(res))

word_list = ['cat','apple','moon','clouds']
long_word(word_list)
