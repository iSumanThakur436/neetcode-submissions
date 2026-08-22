class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        mx= nums[0]*nums[1]
        mi= nums[len(nums)-1]*nums[len(nums)-2]
        return mi-mx
    
        