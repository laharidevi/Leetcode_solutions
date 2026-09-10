class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        r = {0:-1}
        total = 0
        for i,num in enumerate(nums):
            total += num
            rem = total % k
            if rem in r:
                ind = i - r[rem]
                if ind >= 2:
                    return True
            else:
                r[rem] = i
        return False
        
       

        

        