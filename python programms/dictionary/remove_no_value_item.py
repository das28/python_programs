mutidict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
no_value_dict = {k: v for k, v in mutidict.items() if v is not None}
print(no_value_dict)
