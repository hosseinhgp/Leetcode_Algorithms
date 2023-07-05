class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        l=prices[0]
        for i in prices:
            if i<l:
                l=i
            p = max(p, i - l)
        return p
