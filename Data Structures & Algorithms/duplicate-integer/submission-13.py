class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        '''n=len(nums)
        num=sorted(nums)
        for i in range(n-1):
            if num[i]==num[i+1]:
                return True
        return False'''


