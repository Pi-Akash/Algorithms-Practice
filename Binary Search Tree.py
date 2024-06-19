class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        # If the tree is empty then create the first node and assign it to root
        if self.root is None:
            self.root = Node(value)
        else:
            # create a temporary variable to traverse the tree to insert node in proper position
            temp = self.root
            while True:
                # if value already exists in tree, do not insert again and return None
                if temp.value == value:
                    return None
                # if insertion value is greater than temporary variable value then 
                elif value > temp.value:
                    # check if the right sub tree of temporary variable is None or not
                    if temp.right is None:
                        # if its None then we reached child node and we can insert a node in its right sub tree
                        temp.right = Node(value)
                        return True
                    # if not we move out temporary variable to ancester of right sub tree
                    temp = temp.right
                # if insertion value is less than temporary variable value then 
                elif value < temp.value:
                    # check if the left sub tree of temporary variable is None or not
                    if temp.left is None:
                        # if its None then we reached child node and we can insert a node in its left sub tree
                        temp.left = Node(value)
                        return True
                    # if not we move out temporary variable to ancester of left sub tree
                    temp = temp.left
    
    def search(self, value):
        temp = self.root
        while True:
            if temp.value == value:
                return True
            else:
                if value < temp.value:
                    if temp.left is None:
                        return False
                    temp = temp.left
                elif value > temp.value:
                    if temp.right is None:
                        return False
                    temp = temp.right
    
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
    
    def _search(self, value):
        """
        Actual search function called by user.
        """
        return self.__search(self.root, value)
    
    
t = Tree()
t.insert(4)
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(7)

print(t._search(2))