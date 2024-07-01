class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def print_stack(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def push(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def pop(self):
        if self.head is None and self.tail is None:
            return None
        else:
            current = self.head
            self.head = self.head.next
            current.next = None
            return current
    
    def peek(self):
        return self.head
    
ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
print("Stack : ")
ll.print_stack()
print("Peek value : ", ll.peek().value)
                    
    
    