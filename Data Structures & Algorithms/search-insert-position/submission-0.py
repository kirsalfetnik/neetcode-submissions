class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while (l <= r):
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else: 
                l = mid + 1

        if target <= nums[0]:
            return 0
        elif target >= nums[-1]:
            return len(nums)
        
        for i in range(1, len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                continue
            elif target > nums[i-1] and target < nums[i]:
                return i
