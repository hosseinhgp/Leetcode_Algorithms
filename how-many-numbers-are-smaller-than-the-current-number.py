class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        countlist=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count=count+1
            countlist.append(count)
        return countlist 
