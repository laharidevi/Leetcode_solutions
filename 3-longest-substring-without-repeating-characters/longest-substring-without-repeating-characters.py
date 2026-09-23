class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        l = 0
        r = 0
        maxi = 0
        temp = {}
        while r < len(s):
            while temp.get(s[r],0) == 1:
                temp[s[l]] = 0
                l += 1
            temp[s[r]] = 1
            maxi = max(maxi, r-l+1)
            r += 1
        return maxi