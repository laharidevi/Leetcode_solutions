class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def power(n):
            if n == 1:
                return True
            elif n%2 == 0 and n != 0:
                return power(n/2)
            else:
                return False
        if power(n):
            return True
        else:
            return False


                
            
        
        
        
       
        