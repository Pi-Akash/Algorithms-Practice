import random

def quick_sort(arr, pivot_position = "first"):
    if len(arr) <= 1:
        return arr
    else:
        if pivot_position == "first":
            pivot = arr[0]
        elif pivot_position == "last":
            pivot = arr[-1]
        elif pivot_position == "mid":
            mid_index = len(arr) // 2
            pivot = arr[mid_index]
        elif pivot_position == "random":
            random_index = random.randint(0, len(arr)-1)
            pivot = arr[random_index]
        
        print(f"Pivot is {pivot}")
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [4, 6, 1, 7, 3, 2, 5]
print("Original array : ", arr)
print("Sorted array with First pivot : ", quick_sort(arr, "first"))
print("Sorted array with Mid pivot : ", quick_sort(arr, "mid"))
print("Sorted array with Last pivot : ", quick_sort(arr, "last"))
print("Sorted array with Random pivot : ", quick_sort(arr, "random"))
    