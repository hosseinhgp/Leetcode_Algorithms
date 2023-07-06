class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        M=0
        for i in range(len(s)):
            j=i
            count=1
            l=set()
            while s[j] not in l:
                M=max(M,count)
                l.add(s[j])
                j+=1
                count+=1
                if j==len(s):
                    break
        return M
