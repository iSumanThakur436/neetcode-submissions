class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l =0
        r = len(nums) - 1
        while l<=r:
            if nums[(l+r)//2] > target:
                r = ((l+r)//2) - 1
            elif nums[(l+r)//2] < target:
                l = ((l+r)//2) + 1
            else:
                return (l+r)//2
        return -1