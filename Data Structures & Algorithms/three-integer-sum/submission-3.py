class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for i in range(0, len(nums)-2):
            l, r = i + 1, len(nums)-1

            while l < r:
                sumi = nums[i] + nums[l] + nums[r]
                if sumi == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                elif sumi > 0:
                    r -= 1
                elif sumi < 0:
                    l += 1
        return res
            