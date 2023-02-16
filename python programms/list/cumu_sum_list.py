def cumu_sum(lst):
    cum_sum = []
    cumulative = 0 
    for i in lst:
        cumulative += i
        cum_sum.append(cumulative)
    return cum_sum

lst = [1,2,3,4,5,6]
print(cumu_sum(lst))