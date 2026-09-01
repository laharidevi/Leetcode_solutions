class Solution:
    def maxProfit(self, prices: list[int]) -> int:
       l = 0
       r = 1
       maximum = 0
       while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maximum = max(maximum, profit)
        else:
            l = r
        r += 1
       return maximum 
        