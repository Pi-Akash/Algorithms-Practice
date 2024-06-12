class InsertionSort():
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr
    
    def _sort(self, ascending = True):
        if ascending:
            # loop oover array using index variable i
            for i in range(len(self.arr)):
                # temporary index variable j to keep track of the elements and comparision
                j = i - 1
                # while j is not out of bounds and in consecutive values, later is smaller formar then replace the elements
                while j >= 0 and self.arr[j+1] < self.arr[j]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    # decrement j to compare all the elements in array
                    j -= 1
            return self.arr
        else:
            for i in range(len(self.arr)):
                j = i - 1
                while j >= 0 and self.arr[j+1] > self.arr[j]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    j -= 1
            return self.arr

    def _print(self):
        print(self.arr)

print("Original array : ")
arr = [2, 3, 4, 1, 6]
print(arr)

# Sorting array in ascending order using Insertion Sort
print("Ascending order : ")
arr = [2, 3, 4, 1, 6]
obj = InsertionSort(arr)
obj._sort(ascending = True)
obj._print()

# Sorting array in descending order using Insertion Sort
print("Descending order : ")
arr = [2, 3, 4, 1, 6]
obj = InsertionSort(arr)
obj._sort(ascending = False)
obj._print()
