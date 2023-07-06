class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        long = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                long = max(length, long)
        return long
