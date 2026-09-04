class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        while l <= r:
            mid = (l + r) // 2

            if (len(nums) >= 3) and (mid-1 >= 0) and (mid+1 < len(nums)):
                if nums[mid-1] < nums[mid] and nums[mid+1] > nums[mid] and (nums[0] > nums[-1]) and (nums[0] > nums[mid]):
                    r = mid - 1
                elif nums[mid-1] < nums[mid] and nums[mid+1] > nums[mid] and (nums[0] > nums[-1]) and (nums[0] < nums[mid]):
                    l = mid + 1
                elif nums[mid-1] < nums[mid] and nums[mid+1] > nums[mid] and (nums[0] < nums[-1]):
                    r = mid - 1
                elif nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                    return nums[mid+1]
                elif nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
                    return nums[mid]
            
            elif (len(nums) >= 3) and (mid-1 < 0):
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                else:
                    return nums[mid]

            elif (len(nums) >= 3) and (mid+1 >= len(nums)):
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                else:
                    return nums[mid-1]
            
            elif len(nums) == 2:
                if nums[0] > nums[1]:
                    return nums[1]
                else: return nums[0]
            
            elif len(nums) == 1:
                return nums[0]
