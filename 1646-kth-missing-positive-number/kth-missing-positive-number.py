class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = (l + r)//2
            miss = arr[mid]-(mid+1)
            if miss < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k
        