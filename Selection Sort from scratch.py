class SelectionSort:
    def sort(self, arr):
        # loop until the length of the array
        for i in range(len(arr)):
            # select the current pointer index to be minimum value index
            min_index = i
            print("\n")
            print(f"Current Minimum Index : {min_index}")
            print(f"Array after {i}th iteration is : {arr}")
            # loop from index which is next from i to length of array
            for j in range(i, len(arr)):
                # check if there is any element which is smaller than the element at current minimum index position
                if arr[j] < arr[min_index]:
                    # if a smaller value found then update the minimum index position
                    print(f"Item found at index {j} is smaller than the item at {min_index}, so we update the minimum index")
                    min_index = j
            # check if the minimum index is same as the one we started with, this could be possible that the values are already sorted.
            if i != min_index:
                # if not then exchange the elements between current pointer i and minimum value pointer min_index
                arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

arr = [4, 2, 6, 5, 5, 1, 3]
print(f"Original Array : {arr}")
obj = SelectionSort()
obj.sort(arr = arr)