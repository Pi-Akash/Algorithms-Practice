def merge(list1, list2):
    """
    The function merges 2 sorted array and returns a new array with all elements sorted from list1 and list2
    """
    combined = []
    i = 0 
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
            combined.append(list2[j])
            j += 1
    
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    
    return combined

list1 = [1, 3, 7, 8]
list2 = [2, 4, 5, 6]
print(merge(list1, list2))
    