class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique=[]
        res=0
        for i in s:
            while i in unique:
                unique.pop(0)
            unique.append(i)
            res= max(res, len(unique))
        return res


        