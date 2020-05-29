def bubbleSort(list):
    i = len(list)-1
    m = 1

    while i != 0:
        print('iterasi ke-',m)
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            print(list)

        itsSort = True
        for k in range(i):
            if list[k] <= list[k+1]:
                itsSort = itsSort and True
            else:
                itsSort = itsSort and False

        if itsSort:
            print(f'hasil = {list}')
            break

        i -= 1
        m += 1

a = [10,3,5,8,1,20,9,2,4,12]
b = [2,4,8,3,5,6]
bubbleSort(b)
