import random

def quick_sort(arr, pivot_position = "first"):
    if len(arr) <= 1:
        return arr
    else:
        if pivot_position == "first":
            pivot_index = 0
            print(f"Pivot is {pivot_index} at position 0")
        elif pivot_position == "mid":
            mid_index = len(arr) // 2
            pivot_index = mid_index
            print(f"Pivot is {pivot_index} at position {mid_index}")
            
        elif pivot_position == "last":
            pivot_index = -1
            print(f"Pivot is {pivot_index} at position {len(arr) - 1}")
        elif pivot_position == "random":
            random_index = random.randint(0, len(arr))
            pivot_index = random_index
            print(f"Pivot is {pivot_index} at position {random_index}")
    
    pivot = arr.pop(pivot_index)
    left = [x for x in arr if x[0] < pivot[0]]
    right = [x for x in arr if x[0] > pivot[0]]
    
    return quick_sort(left) + [pivot] + quick_sort(right) 

arr = [(1, "a"), (3, "n"), (7, "v"), (8, "l"), (2, "o"), (4, "p"), (5, "e"), (6, "s")]
print("Original array : ", arr)
print("Sorted array with First pivot : ", quick_sort(arr, "first"))

arr = [(1, "a"), (3, "n"), (7, "v"), (8, "l"), (2, "o"), (4, "p"), (5, "e"), (6, "s")]
print("Sorted array with Mid pivot : ", quick_sort(arr, "mid"))

arr = [(1, "a"), (3, "n"), (7, "v"), (8, "l"), (2, "o"), (4, "p"), (5, "e"), (6, "s")]
print("Sorted array with Last pivot : ", quick_sort(arr, "last"))

arr = [(1, "a"), (3, "n"), (7, "v"), (8, "l"), (2, "o"), (4, "p"), (5, "e"), (6, "s")]
print("Sorted array with Random pivot : ", quick_sort(arr, "random"))
