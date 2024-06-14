def binary_search(arr, search):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if search == arr[mid]:
            return True
        elif search > arr[mid]:
            left = mid + 1
        elif search < arr[mid]:
            right = mid - 1
    return False    
        
arr = [1, 2, 3, 4, 5, 6]
print(binary_search(arr, 5))