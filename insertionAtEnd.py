class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def insertionAtLast(self, newData):
        NewNode = Node(newData)
        if self.head == None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode


lList = LinkedList()
lList.head = Node("RRR")
second = Node("Magadheera")
third = Node("Bahubali")

lList.head.next = second
second.next = third

lList.insertionAtLast("Athidi")

lList.display()
