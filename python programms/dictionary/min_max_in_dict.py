fruitsDict = {'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
min_key = min(fruitsDict, key=fruitsDict.get)
max_key = max(fruitsDict, key=fruitsDict.get)
print("Min key:", min_key)
print("Max key:", max_key)