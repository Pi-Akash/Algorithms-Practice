class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def __insert(self, current_node, value):
        if self.root is None:
            current_node = Node(value)
            return True
        
        if value == current_node.value:
            return False
                
        if value < current_node.value:
            current_node.left = self.__insert(current_node.left, value)
        
        if value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
                return True
            self.__insert(current_node.right, value)
            
    
    def insert(self, value):
        self.__insert(self.root, value)
    
    def __search(self, current_node, value):
        """
        Helper function for the recursive search
        """
        # if the current node is None
        if current_node is None:
            return False
        
        # if the current node value is what we are searching for
        if value == current_node.value:
            return True
        
        # if the search value is lower than the current node value then we want to recursively search in the left subtree
        if value < current_node.value:
            return self.__search(current_node.left, value)
        
        # if the search value is greater than the current node value then we want to recursively search in the right subtree
        if value > current_node.value:
            return self.__search(current_node.right, value)
    
    def search(self, value):
        """
        Actual search function called by user.
        """
        return self.__search(self.root, value)
    
t = Tree()
print(t.insert(4))
print(t.insert(1))
print(t.insert(2))
print(t.insert(3))
print(t.insert(7))

print(t.search(2))