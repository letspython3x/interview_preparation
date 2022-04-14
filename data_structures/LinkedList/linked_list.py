from contextlib import nullcontext
from distutils.dist import DistributionMetadata


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        print("Linked List elements")
        node = self.head
        while node.nextNode:
            print(node.data)
            node = node.nextNode
        print(node.data)
    
    def insert_begining(self, item):
        newNode = Node(item)
        newNode.nextNode = self.head
        self.head = newNode
    
    def insert_end(self, item):
        newNode = Node(item)
        node = self.head
        while node.nextNode:
            node = node.nextNode
        node.nextNode = newNode
    

def create_nodes(myList):
    ll = LinkedList()
    
    for pos, item in enumerate(myList):
        if pos == 0:
            node = Node(item)
            ll.head = node 
        else:
            temp_node = Node(item)
            node.nextNode = temp_node
            node = temp_node
    return ll


ll = create_nodes([1,2,3,4])
ll.traverse()
ll.insert_begining(10)
ll.traverse()
ll.insert_end(11)
ll.traverse()