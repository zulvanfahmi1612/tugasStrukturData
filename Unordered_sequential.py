def modUO_Sequential(listData, key):
    result = []

    for i in range(len(listData)):
        if listData[i] == key:
            result.append(i)

    if len(result) == 0:
        return "not found"
    else:
        return f"data is in index {result}"


a = [54, 25, 73, 12, 15, 2, 30, 73]
print(modUO_Sequential(a, 73))
