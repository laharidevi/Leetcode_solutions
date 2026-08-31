class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = ""
        m = len(word1)
        n = len(word2)
        if m != n:
            l = min(m,n)
        else:
            l = m
        for i in range(l):
            a += word1[i] + word2[i]
        if m > n:
            return a + word1[n:m]
        elif m < n:
            return a + word2[m:n]
        else:
            return a

        
        