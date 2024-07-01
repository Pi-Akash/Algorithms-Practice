class Solution:
    def threeConsecutiveOdds_1(self, arr):
        l = 0
        r = 3
        while r <= len(arr):
            counter = 0
            for i in range(l, r):
                if arr[i] % 2 != 0:
                    counter += 1
            
            #print(f"For current window : {arr[l:r]}, the count is {counter}.")
            if counter == 3:
                return True
            else:
                l += 1
                r += 1
        return False
    
    def threeConsecutiveOdds_2(self, arr):
        for i in range(len(arr)-2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                 return True
                    
s = Solution()
print(s.threeConsecutiveOdds_1([1, 2, 3, 10, 5, 7, 9, 12]))
print()
print(s.threeConsecutiveOdds_2([1, 1, 1]))