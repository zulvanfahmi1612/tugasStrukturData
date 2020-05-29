def createQueue():
    q=[]
    return q

def enqueue(q,data):
    q.insert(0, data)
    return q

def dequeue(q):
    data = q.pop()
    return data

def isEmpty(q):
    return (q==[])

def size(q):
    return (len(q))


def ularNaga(player, count):
    print(f"pemain : {player} \n")
    while size(player) > 1:
        for i in range(count):
            enqueue(player, dequeue(player))
            print(f"Proses hitung ke-{i+1},  {player}")

        print("")
        dequeue(player)
        print(f"Pemain saat ini : {player}\n")

    return f"pemenang : {str(player)}"

a = ["bambang", "eko", "narti", "siti", "supeno"]
print(ularNaga(a, 3))
