def modSequentialSearch_OL(listData, key):
    i = 0
    count = 0
    result = []

    while True:
        if i == len(listData) or listData[i] > key:
            break
            # utk menghentikan iterasi

        elif listData[i] == key:
            result.append(i)
        i += 1
        count += 1

    print(f"counter - {count}")
    if len(result) != 0:
        return f"key = {key}, berada di indeks {result}"
    else:
        return "data tidak ditemukan"


a = [2, 12, 15, 15, 15, 25, 30, 54, 73]
print(modSequentialSearch_OL(a, 15))
