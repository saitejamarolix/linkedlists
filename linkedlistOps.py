class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertStart(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
        
    def insertNext(self,previousData,newData):
        if previousData is None:
            print("previous node isn't present, so new node cannot be added")
            return
        else:
            newNode = Node(newData)
            newNode.next = previousData.next.next
            previousData.next = newData
            
    def display(self):
        temp = self.head
        while temp:
            print(str(temp.data))
            temp = temp.next
            
linked_list = LinkedList()
linked_list.insertStart("Sai Teja")
linked_list.display()
print("----------------------------")
linked_list.insertNext(linked_list.head.next, "Arjun")
linked_list.display()
