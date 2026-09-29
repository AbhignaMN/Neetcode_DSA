class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        
        ordered=sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(ordered[i][0])
        return result