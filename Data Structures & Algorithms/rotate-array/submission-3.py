class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        test = [0] * len(nums)
        for i in range(0, len(nums)):
            test[(i + k) % (len(nums))] = nums[i]
        nums[:] = test