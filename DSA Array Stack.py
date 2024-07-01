class Array_Stack:
    def __init__(self):
        self.stack = []
        self.length = 0
    
    def push(self, value):
        self.stack.append(value)
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        node = self.stack.pop()
        self.length -= 1
        return node
    
    def peek(self):
        return self.stack[-1]
        
a = Array_Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
print("Stack : ", a.stack)
print("Stack Peek : ", a.peek())

