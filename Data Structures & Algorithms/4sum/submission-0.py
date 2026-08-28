class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        first = 0
        
        while first < len(nums):
            second = first + 1

            while second < len(nums):
                l = second + 1
                r = len(nums) - 1

                while (l < r):
                    fourSum = nums[first] + nums[second] + nums[l] + nums[r]
                    if (fourSum < target):
                        l += 1
                    elif (fourSum > target):
                        r -= 1
                    else:
                        res.append([nums[first], nums[second], nums[l], nums[r]])
                        l += 1
                        while (l < r and nums[l-1] == nums[l]):
                            l += 1
        
                second += 1
                while (second < len(nums) and nums[second-1] == nums[second]):
                    second += 1

            first += 1
            while (first < len(nums) and nums[first-1] == nums[first]):
                    first += 1

        return res
