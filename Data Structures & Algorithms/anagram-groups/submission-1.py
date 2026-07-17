class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in strs:
            c =[0]*26
            for ch in i :
                c[ord(ch)-ord('a')]+=1
            
            group[tuple(c)].append(i)
        return list(group.values())

            
        
