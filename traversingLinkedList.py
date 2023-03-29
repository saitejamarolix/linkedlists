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

lList = LinkedList()
lList.head = Node("CHandigarh")
second = Node("Hyderabad")
third = Node("Banglore")

lList.head.next = second
second.next = third

lList.display()

