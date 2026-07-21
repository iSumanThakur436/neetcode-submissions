class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique= set()
        left = 0
        res=0
        for i in range(len(s)):
            while s[i] in unique:
                unique.remove(s[left])
                left+=1
            unique.add(s[i])
            res= max(res, len(unique))
        return res


        