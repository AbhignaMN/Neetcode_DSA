class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):

        stack = []
        nextGreater = {}

        # Traverse nums2 from right to left
        for i in range(len(nums2) - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                nextGreater[nums2[i]] = stack[-1]
            else:
                nextGreater[nums2[i]] = -1

            stack.append(nums2[i])

        ans = []

        for num in nums1:
            ans.append(nextGreater[num])

        return ans