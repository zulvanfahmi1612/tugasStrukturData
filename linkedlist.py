class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def getData(self): # getter, untuk memperoleh info data
        return self.data

    def getNext(self): # utk mmproleh info data selanjutnya
        return self.next

    def setData(self, item): # setter, mengganti data
        self.data = item

    def setNext(self, pt): # mengganti data selanjutnya
        self.next = pt

class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addNode(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def listprint(self):
        printli = self.head
        print("(Head)", end=" ")
        while printli is not None:
            print(printli.data, end=" -> ")
            printli = printli.next
        print("(None)")



mylist = LinkedList()
mylist.addNode(12)
mylist.addNode(45)
mylist.addNode(72)

print(mylist.size())
mylist.listprint()
