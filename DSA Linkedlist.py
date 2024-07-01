class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def get_value(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
        elif index == self.length-1:
            self.append(value)
        else:
            prev_node = self.get(index - 1)
            next_node = self.get(index)
            
            new_node.next = next_node
            prev_node.next = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            current = self.head
            self.head = None
            self.tail = None
        else:
            prev = None
            current = self.head
            while current.next is not None:
                prev = current
                current = current.next
            
            prev.next = None
            self.tail = prev
        self.length -= 1
        return current

    def removeHead(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            current = self.head
            self.head = None
            self.tail = None
        else:
            current = self.head
            self.head = self.head.next
            current.next = None
        self.length -= 1
        return current

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            current = self.removeHead()
        elif index == self.index - 1:
            current = self.pop()
        else:
            prev_node = self.get(index - 1)
            next_node = self.get(index + 1)
            current = self.get(index)
            current.next = None
            prev_node.next = next_node
        self.length -= 1
        return current
    
    def reverse(self):
        prev_node = None
        current = self.head
        next_node = current.next
        
        while current is not None:
            current.next = prev_node
            prev_node = current
            current = next_node
            if next_node is not None:
                next_node = next_node.next
        
        self.head, self.tail = self.tail, self.head
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        
ll = LinkedList()
ll.append(2)
ll.prepend(1)
ll.append(3)
ll.append(4)
print("Length of list : ", ll.length)
ll.reverse()
            