def convDectoBiner(desimal):
    num_display = desimal
    result = []

    while desimal > 0:
        if desimal % 2 == 0:
            result.insert(0, 0)
            desimal /= 2

        elif desimal == 1:
            result.insert(0, 1)
            desimal = 0

        elif desimal % 2 == 1:
            result.insert(0, 1)
            desimal = (desimal / 2) - 0.5


    #print(result)
    a = [str(integer) for integer in result]
    b = "".join(a)
    return f"{num_display} desimal = {int(b)} biner"



num = int(input("masukkan angka : "))
print(convDectoBiner(num))
