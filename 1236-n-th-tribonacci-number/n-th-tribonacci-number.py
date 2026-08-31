class Solution:
    def tribonacci(self, n: int) -> int:
        a = [-1] * (n+1)
        def tri(n):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            if a[n] != -1:
                return a[n]
            a[n] = tri(n-3) + tri(n-2) + tri(n-1)
            return a[n]
        return tri(n)
            
      
            

