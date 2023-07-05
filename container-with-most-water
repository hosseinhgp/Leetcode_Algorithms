class Solution:
    def maxArea(self, height: List[int]) -> int:
        j=len(height)-1
        i=0
        vol=0
        while i<j:
            vol=max(((j-i)*min(height[j],height[i])),vol)
            if height[i]>=height[j]:
                j=j-1
            else:
                i=i+1
        return vol
