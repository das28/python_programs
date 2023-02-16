import random
def random_num(n):
    random_lst = []
    for i in range(n):
        random_number = random.randint(1,20)
        random_lst.append(random_number)
    return True


print(random_num(10))
