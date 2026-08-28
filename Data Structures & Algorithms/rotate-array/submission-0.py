class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        split = len(nums) - k
        nums[:] = nums[split:len(nums)] + nums[0:split]