class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        # dp[i] = minimum cost to reach step i
        dp = [0] * n

        # Base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Fill the DP array
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        # Top can be reached from the last or second last step
        return min(dp[n - 1], dp[n - 2])