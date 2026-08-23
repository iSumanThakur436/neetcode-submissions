class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sn= ''.join(sorted(s))
        tn= ''.join(sorted(t))
        return sn == tn
        