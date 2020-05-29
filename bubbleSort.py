def bubbleSort(list):

    for i in reversed(range(1, len(list))):
        print('iterasi ke-', len(list)-i, 'jumlah iterasi-', i )
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

            print(j+1, '=', list)
    return list


a = [10,2,1,13,15,22,11,45]
print(f'hasil = {bubbleSort(a)}')
