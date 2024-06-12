# for i in range(len(arr), 0, -1):
#     print("Current i : ", i)
#     for j in range(1, i):
#         print("current j : ", j)
#         if arr[j-1] > arr[j]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#         print("arr after current swap : ", arr)
#     print(f"arr for {i}th iteration: {arr}")

# #print(arr)

class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
    
    def _sort(self):
        # loop start from the length of array to 0
        for i in range(len(self.arr), 0, -1):
            print(f"Current i : {i}")
            # sub loop starting from 1 to ith index
            for j in range(1, i):
                print(f"Current j : {j}")
                if self.arr[j-1] > self.arr[j]:
                    self.arr[j], self.arr[j-1] = self.arr[j-1], self.arr[j]
                print(f"After current subloop and swap array: {self.arr}")
            print(f"Array for {i}th iteration : {self.arr}")
    
    def _print(self):
        print("Sorted array : ")
        print(self.arr)
    
print("Original array : ")
arr = [2, 3, 4, 6, 1]
print(arr)

obj = BubbleSort(arr)
obj._sort()
obj._print()