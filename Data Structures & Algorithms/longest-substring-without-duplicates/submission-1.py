class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        max_len=0
        left=0
        
        cur_len=0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
                
            seen.add(s[right])
            cur_len=right-left+1
            max_len=max(cur_len,max_len)
        return max_len