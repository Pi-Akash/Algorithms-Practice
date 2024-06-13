def merge(l1, l2):
    combined = []
    i = 0
    j = 0
    
    if len(l1) == 0:
        while i < len(l1):
            combined.append(l1[i])
            i += 1
    
    if len(l2) == 0:
        while j < len(l2):
            combined.append(l2[j])
            j += 1
    
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            combined.append(l1[i])
            i += 1
        elif l2[j] <= l1[i]:
            combined.append(l2[j])
            j += 1
    
    while i < len(l1):
        combined.append(l1[i])
        i += 1
    
    while j < len(l2):
            combined.append(l2[j])
            j += 1
    
    return combined

def sort(arr):
    if len(arr) == 1:
        return arr

    mid_index = len(arr) // 2
    left_array = sort(arr[:mid_index])
    right_array = sort(arr[mid_index:])
    return merge(left_array, right_array)
    
l1 = [(1, "a"), (3, "n"), (7, "v"), (8, "l")]
l2 = [(2, "o"), (4, "p"), (5, "e"), (6, "s")]
#print(merge(l1, l2))

arr = [(1, "a"), (3, "n"), (7, "v"), (8, "l"), (2, "o"), (4, "p"), (5, "e"), (6, "s")]
print(sort(arr))
    