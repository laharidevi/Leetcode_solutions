
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * 1024 for _ in range(n)]

        dp[0][grid[0][0]] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                x = grid[i][j]
                curr = [0] * 1024

                if i > 0:
                    for v in range(1024):
                        if dp[j][v]:
                            curr[v ^ x] = 1

                if j > 0:
                    for v in range(1024):
                        if dp[j - 1][v]:
                            curr[v ^ x] = 1

                dp[j] = curr

        for v in range(1024):
            if dp[n - 1][v]:
                return v
