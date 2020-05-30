def ascMin(data):
    print(f"{len(data)} data = {data}")
    print(f"jumlah iterasi luar = {len(data)-1}")
    print("")

    for outerLoop in range(len(data)-1):
        num = outerLoop

        for inn in range(outerLoop+1, len(data)):
            #print(outerLoop, inn)
            if data[num] > data[inn]:
                num = inn
        data[outerLoop], data[num]  = data[num], data[outerLoop]

        temp = []
        for b in range(outerLoop+1, len(data)):
            temp.append(b)
        print(f"iterasi luar ke- {outerLoop + 1}, {len(data)-(outerLoop + 1)} iterasi dalam, membanddingkan indeks-{outerLoop} dengan indeks-{temp}")
        print(f"hasil = {data}")
        print("")


a = [1, 7, 13, 17, 23, 27, 32]
ascMin(a)
