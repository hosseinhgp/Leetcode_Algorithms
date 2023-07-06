class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        #by list
        newnum=[]
        for i in nums:
            if i in newnum:
                return True
            else:
                newnum.append(i)
        return False
         ''' 
        #by set
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
