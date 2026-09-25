class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sums = 0
            while num != 0:
                sums += num % 10
                num = num//10
            num = sums 
        return num
       
        