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
            
    def insertAtStart(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
        
    def insertionAtLast(self, newData):
        NewNode = Node(newData)
        if self.head == None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode           

    def insertionAtBetween(self, middleNode ,newData):
        if middleNode is None:
            print("not possible to add in between")
            return

        NewNode = Node(newData)
        NewNode.next = middleNode.next
        middleNode.next = NewNode

        


lList = LinkedList()
lList.head = Node("Balagam")
second = Node("Lovetoday")
third = Node("ColorPhoto")
fourth = Node("Solo")

lList.head.next = second
second.next = third
third.next = fourth


lList.insertAtStart("nenokkadine")
lList.insertionAtLast("nenokkadine")
lList.insertionAtBetween(lList.head.next,"nenokkadine")

lList.display()



# arguement = real values
# paramaeters or params = derived