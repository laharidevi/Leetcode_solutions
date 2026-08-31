class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = ""
        m = len(word1)
        n = len(word2)
        l = max(m,n)
        for i in range(l):
            if i < m:
                a += word1[i]
            if i < n:
                a += word2[i]
        return a

        
        