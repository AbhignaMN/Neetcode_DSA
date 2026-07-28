class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []
        path = []

        def dfs(index, target):

            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(index, len(nums)):

                path.append(nums[i])

                # same i because we can reuse the number
                dfs(i, target - nums[i])

                path.pop()

        dfs(0, target)

        return res