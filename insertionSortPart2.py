def ascAwal(data):
    print(f"data awal = {data}")
    print(f"jumlah iterasi luar = {len(data)-1}")
    print("")

    for i in range(1, len(data)):
        count = 0
        key = data[i]
        j = i - 1
        while j >= 0 and key <= data[j]:
            data[j+1] = data[j]
            j -= 1
            count += 1
        data[j+1] = key

        print(f"iterasi ke-{i}, {count} kali iterasi dalam : ", end="")
        temp = []
        for j in range(i+1):
            temp.append(data[j])
        print(temp)
        del temp

    print(f"hasil = {data}")

a = [3, 89, 678, 2400, 65, 101, 21]
ascAwal(a)
