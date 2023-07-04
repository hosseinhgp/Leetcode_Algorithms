class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l= len(nums)
        sortednum=sorted(nums)
        high=0
        low=l
        for i in range(l):
            if nums[i]!=sortednum[i]:
                low=min(i,low)
                high=max(i,high)
        if high==0:
            return 0
        else:
            return high-low+1   
