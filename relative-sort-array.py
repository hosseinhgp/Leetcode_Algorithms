class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        extra = [i for i in arr1 if i not in arr2]
        origin = arr2[:]
        extra.sort()
        keys = origin + extra
        arr1.sort(key=lambda x: keys.index(x))
        return arr1
