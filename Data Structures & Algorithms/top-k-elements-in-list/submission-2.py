class Solution:
    def topKFrequent(self, nums, k):
        
        # Step 1: frequency map
        freq = {}
        for num in nums:
            if num in freq: 
                freq[num]+=1 
            else: 
                    freq[num]=1
        
        # Step 2: bucket
        bucket = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: fill bucket
        for num, count in freq.items():
            bucket[count].append(num)
        
        # Step 4: collect result
        result = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        
        
        