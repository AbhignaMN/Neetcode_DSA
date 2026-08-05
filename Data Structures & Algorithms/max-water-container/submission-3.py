class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxArea=0
       
        while left<right:
            h = min(heights[left], heights[right])
            width=(right-left)
            area=width*h
            if (heights[left]<heights[right]):
                left+=1
            else:
                right-=1
            maxArea=max(area,maxArea)
        return maxArea
            
        