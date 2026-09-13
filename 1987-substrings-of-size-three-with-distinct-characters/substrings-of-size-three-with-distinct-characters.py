class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp = []
                for k in range(i,j+1):
                    temp.append(s[k])
                if len(temp) == 3 and len(set(temp)) == 3:
                    c += 1
        return c


        