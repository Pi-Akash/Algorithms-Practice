# Sorting tuples in a list using Insertion sort 
class Solution:
    def insertionSort(self, pairs):
        states = []
        for i in range(len(pairs)):
            j = i-1
            states.append(pairs)
            while j >= 0 and pairs[j+1][0] < pairs[j][0]:
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]
                j -= 1
            print(pairs)
        return states

    def bubblesortDescending(self, pairs):
        for i in range(0, len(pairs)):
            for j in range(1, i):
                if pairs[j-1][0] > pairs[j][0]:
                    pairs[j-1], pairs[j] = pairs[j], pairs[j-1]
            print(pairs)
        return pairs

    def bubblesortAscending(self, pairs):
        for i in range(len(pairs), 0, -1):
            for j in range(1, i):
                if pairs[j-1][0] > pairs[j][0]:
                    pairs[j-1], pairs[j] = pairs[j], pairs[j-1]
            print(pairs)
        return pairs
    
print("Insertion Sort : ")
pairs=[(5, "apple"), (2, "banana"), (9, "cherry")]
obj = Solution()
obj.insertionSort(pairs = pairs)

print("Bubble Sort Descending : ")
pairs=[(3, "cat"), (3, "bird"), (2, "dog")]
obj = Solution()
obj.bubblesortDescending(pairs = pairs)

print("Bubble Sort Ascending : ")
pairs=[(3, "cat"), (3, "bird"), (2, "dog")]
obj = Solution()
obj.bubblesortAscending(pairs = pairs)
