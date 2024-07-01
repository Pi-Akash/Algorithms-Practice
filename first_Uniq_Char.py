class Solution:
    def firstUniqChar(self, s):
        char_map = {}
        for element in s:
            if element not in char_map:
                char_map[element] = 1
            else:
                char_map[element] += 1
        
        print(char_map)
        for k in char_map.keys():
            if char_map[k] == 1:
                print(k)
                print(s.index(k))
        
        return -1
        
s = Solution()
s.firstUniqChar("google")
s.firstUniqChar("dddccdbba")