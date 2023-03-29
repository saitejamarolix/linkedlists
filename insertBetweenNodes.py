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

    def insertionAtBetween(self, middleNode ,newData):
        if middleNode is None:
            print("not possible to add in between")
            return

        NewNode = Node(newData)
        NewNode.next = middleNode.next
        middleNode.next = NewNode

        


lList = LinkedList()
lList.head = Node("RRR")
second = Node("Magadheera")
third = Node("Bahubali")

lList.head.next = second
second.next = third

lList.insertionAtBetween(lList.head.next,"Athidi")

lList.display()



# arguement = real values
# paramaeters or params = derived