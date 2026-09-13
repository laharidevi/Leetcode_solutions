class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = 0
        l = 0
        r = k-1
        for i in range(l,r+1):
            sums += nums[i]
        maxi = sums
        while r < len(nums)-1:
            sums -= nums[l]
            l+=1
            r += 1
            sums += nums[r]
            maxi = max(maxi,sums)
        return maxi / k
                
                


                