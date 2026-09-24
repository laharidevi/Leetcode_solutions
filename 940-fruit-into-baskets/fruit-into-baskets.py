class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l = 0
        r = 0
        maxi = 0
        temp = {}
        while r < len(fruits):
            if fruits[r] in temp:
                temp[fruits[r]] += 1
            else:
                temp[fruits[r]] = 1
            while len(temp) > 2:
                temp[fruits[l]] -= 1
                if temp[fruits[l]] == 0:
                    del temp[fruits[l]] 
                l += 1
            maxi = max(maxi, r-l+1)
            r += 1
        return maxi
     
        