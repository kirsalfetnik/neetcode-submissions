class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if (j != i) and (nums[j] == nums[i]):
                    return True
        return False