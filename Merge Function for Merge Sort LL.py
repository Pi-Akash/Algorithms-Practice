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
    
    def pop(self):
        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
        self.tail = prev
        self.length -= 1
        return current
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
    
    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            prev_node = self.get(index = index - 1)
            next_node = self.get(index = index + 1)
            
            if next_node is None:
                self.append(value)
            else:
                # insertion process
                new_node.next = next_node
                prev_node.next = new_node
                self.length += 1
            return True
    
    def remove(self, index):
        if index <= 0 or index >= self.length:
            return False
        else:
            prev_node = self.get(index = index - 1)
            next_node = self.get(index = index + 1)
            current = self.get(index)
            
            # deletion process
            prev_node.next = next_node
            self.length -= 1
            return True
            
ll1 = LinkedList()
ll1.append(3)
ll1.prepend(1)
ll1.append(7)
ll1.insert(2, 8)
#ll1.print_list()

ll2 = LinkedList()
ll2.append(4)
ll2.prepend(2)
ll2.append(5)
ll2.insert(2, 6)
#ll2.print_list()

def merge_sorted_ll(list1, list2):
    combined = Node("Dummy")
    combined_current = combined
    current_l1 = list1.head
    current_l2 = list2.head
    
    while current_l1 is not None and current_l2 is not None:
        if current_l1.value <= current_l2.value:
            combined_current.next = current_l1
            current_l1 = current_l1.next
        elif current_l2.value < current_l1.value:
            combined_current.next = current_l2
            current_l2 = current_l2.next
        combined_current = combined_current.next
        
        
    if current_l1 is not None:
        combined_current.next = current_l1
            
    if current_l2 is not None:
        combined_current.next = current_l2

    merged_list = LinkedList()
    merged_list.head = combined.next
    current = merged_list.head
    while current is not None:
        print(current.value)
        current = current.next
    
merge_sorted_ll(list1 = ll1, list2 = ll2)
        
    