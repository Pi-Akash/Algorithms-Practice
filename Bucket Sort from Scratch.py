def bucket_sort(arr):
    distinct_values = len(set(arr))
    buckets = [0] * distinct_values
    
    for element in arr:
        buckets[element] += 1
    
    arr = []
    for element, count in enumerate(buckets):
        arr += [element] * count
    
    return arr

arr = [2, 1, 2, 0, 0, 2, 4, 3, 4]
print(bucket_sort(arr))