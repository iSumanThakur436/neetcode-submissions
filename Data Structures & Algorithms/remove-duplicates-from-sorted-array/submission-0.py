class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        snums= set()
        for i in nums[:]:
            if i in snums:
                nums.remove(i)
            else:
                snums.add(i)
        return len(nums)
        

        