class Node:
    #creating a node

    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# create an object from derived class
llist = LinkedList()
llist.head = Node("Pawan Kalyan ")
second = Node("Srinivasan B ")
third = Node("NIhar ")
fourth = Node("Ranjan ")

#connetcing the nodes
llist.head.next = second
second.next = third
third.next = fourth
# print
while llist.head!=None:
    print(llist.head.item)
    llist.head = llist.head.next
    
    
# ex:-

class Node:
    
    def __inti__(self,item):
        self.item = item
        self.next = None

class link_Box:
    def __init__(self):
        self.head = None
        
linked = link_Box()
linked.head = Node("Gold ")
second = Node("money")
third = Node("land documents")

linked.head.next = second
second.next = third

while linked.head!=None:
      print(linked.head.item)
      linked.head = linked.head.next
      
    