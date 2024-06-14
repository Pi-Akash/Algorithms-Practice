def pivot(arr):
    pivot = 0
    swap = 0
    
    for i in range(1, len(arr)):
        if arr[i] < arr[pivot]:
            swap += 1
            arr[swap], arr[i] = arr[i], arr[swap]
        else:
            continue
    
    arr[swap], arr[pivot] = arr[pivot], arr[swap]

    return arr

arr = [4, 6, 1, 7, 3, 2, 5]
print("Original Array : ", arr)
print("Array after pivot : ", pivot(arr))