class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        while start<end:
            if nums[start]<nums[end]:
                return nums[start]
            if nums[end]<nums[end-1]:
                return nums[end]
            start+=1
            end-=1
        return nums[start]
