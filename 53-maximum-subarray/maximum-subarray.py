class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = nums[0]
        sums = nums[0]
        for i in range(1,len(nums)):
            if sums >= 0:
                sums += nums[i]
            else:
                sums = nums[i]
            if maxi < sums:
                maxi = sums
        return maxi
            
        