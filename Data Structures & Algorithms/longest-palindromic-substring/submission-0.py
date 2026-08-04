class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) < 2:
            return s

        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):

            # Odd length
            len1 = expand(i, i)

            # Even length
            len2 = expand(i, i + 1)

            maxLen = max(len1, len2)

            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2

        return s[start:end + 1]