class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for i in range(0, len(nums)-2):
            l, r = i + 1, len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                sumi = nums[i] + nums[l] + nums[r]
                if sumi == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sumi > 0:
                    r -= 1
                elif sumi < 0:
                    l += 1
        return res
            