class Solution:
    def binary_search(self, nums, target):
        #print(nums)
        if len(nums) <= 1:
            if nums[0] == target:
                return True
            else:
                return False
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            #print(target == nums[mid])
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return False

    def searchMatrix(self, matrix, target):
        for mat in matrix:
            if target >= mat[0] and target <= mat[-1]:
                value = self.binary_search(mat, target)
                break
            else:
                value = False
        return value

# Case 1
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
s = Solution()
print(s.searchMatrix(matrix, target))