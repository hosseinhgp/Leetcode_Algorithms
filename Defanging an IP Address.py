class Solution:
    def defangIPaddr(self, address: str) -> str:
        newstring=''
        for i in range(len(address)):
            if address[i]== '.':
                newstring= newstring + '[.]'
            else:
                newstring= newstring +address[i]
        return newstring
