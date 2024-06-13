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
    #print(combined)
    return combined

def sort(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr
    print()
    mid_index = len(arr) // 2
    print(f"Mid Index : {mid_index}")
    left_array = sort(arr[:mid_index])
    print(f"Left array :", left_array)
    right_array = sort(arr[mid_index:])
    print(f"Right array : ", right_array)
    return merge(left_array, right_array)

arr = [5, 4, 7, 1, 3, 2, 8, 6]
print(sort(arr))
        
        