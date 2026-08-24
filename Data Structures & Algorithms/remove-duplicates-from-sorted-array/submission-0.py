class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 1

        while (L < R and L < len(nums) and R < len(nums)):
            if nums[L] != nums[R]:
                L += 1
                R += 1
            elif nums[L] == nums[R]:
                nums.pop(R)
        return len(nums)