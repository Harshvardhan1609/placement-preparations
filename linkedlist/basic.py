class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtBeginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def printLL(self):
        current_Node = self.head
        while current_Node:
            print(current_Node.data)
            current_Node = current_Node.next
    
if __name__ == '__main__':
    l1 = LinkedList()
    l1.insertAtBeginning(1)
    l1.insertAtBeginning(2)
    l1.insertAtBeginning(3)
    l1.printLL()
