class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)% len(nums)]:
                return nums[(i+1)% len(nums)]
        return nums[0]
        