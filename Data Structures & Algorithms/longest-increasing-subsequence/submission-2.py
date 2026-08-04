from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(i):
            ans = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, 1 + dfs(j))

            return ans

        res = 0

        for i in range(len(nums)):
            res = max(res, dfs(i))

        return res
