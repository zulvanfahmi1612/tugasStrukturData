import queue as qq
#  a5 b4 c2


def makeTask(numOfTask):
    print('Buat task')
    task = {}
    for i in range(numOfTask):
        print(f'task ke-{i+1}')
        a = str(input('masukkan nama task : '))
        b = int(input('masukkan nilai task : '))
        task[a] = [a, b, 0]
    return task


def scheduling(listTask,time):
    print(f"waktu proses cpu = {time}")
    print(f"antrian proses : {listTask.values()}")
    counter = 1
    totalTime = 0
    listName = qq.createQueue()
    for i in listTask:
        qq.enqueue(listName, i)
    #print(listName)
    #print(listTask)
    #print(' ')

    while not qq.isEmpty(listName):
        print(f"iterasi ke - {counter}")
        counter += 1

        name = qq.dequeue(listName)
        value = listTask[name][1]
        print(f"proses {name} sedang dikerjakan, sisa waktu proses {name} = {value}")


        if value > time:
            totalTime += time

            value = value - time
            listTask[name][1] = value

            qq.enqueue(listName, name)
            print(f"antrian data tersisa : {listName}")
            print(f"sisa task {listTask}")

        elif value <= time:
            totalTime += value

            listTask[name][1] = 0
            listTask[name][2] = totalTime

            print(f"proses {name} selesai")
            print(f"antrian data tersisa : {listName}")
            print(f"sisa task {listTask}")


    return listTask



p = int(input("masukkan proses yang dijadwalkan di cpu : "))
task = makeTask(p)
#task = {'a': [5, 0], 'b': [4, 0], 'c': [2, 0]}

print(scheduling(task, 3))
