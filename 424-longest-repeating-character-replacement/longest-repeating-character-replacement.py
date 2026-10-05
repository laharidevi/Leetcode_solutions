class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        count = {}
        cnt = 0
        maxi = 0
        max_count = 0
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            max_count = max(max_count, count[s[r]])
            while r-l+1 - max_count > k:
                count[s[l]] -= 1
                l += 1
            maxi = max(maxi, r-l+1)
            r += 1
        return maxi