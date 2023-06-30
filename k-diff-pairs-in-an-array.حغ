class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        if k == 0:
            count = {}
            for a in nums:
                if a not in count:
                    count[a] = 0
                count[a] = count[a]+1
            for b in count:
                if count[b] > 1:
                    ans = ans+1
            return ans
        if k < 0:
            return 0
        nums = set(nums)
        for aa in nums:
            if aa + k in nums:
                ans += 1
            if aa - k in nums:
                ans += 1
        return ans // 2    
