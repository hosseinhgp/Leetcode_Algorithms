# time opmitum
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

# first solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False    
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=[]
        checked=[]
        n=len(strs)
        for i in range(n):
            if i in checked:
                continue
            anargamlist=[strs[i]]
            checked.append(i)
            for j in range(i+1,n):
                if self.isAnagram(strs[i],strs[j]) and j not in checked:
                    anargamlist.append(strs[j])
                    checked.append(j)
            out.append(anargamlist)
        return out
