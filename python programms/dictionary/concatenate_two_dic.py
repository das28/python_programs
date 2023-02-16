def concat_dic(dic1,dic2):
    return {**dic1, **dic2}

dic1 = {"a":1, "b":2, "c":3}
dic2 = {"d":4, "e":5, "f":6}

print(concat_dic(dic1,dic2))