class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []

        for i in range(0, len(nums)-1):
            l, r = i+1, len(nums)-1

            if (i > 0):
                if nums[i] == nums[i-1]:
                    continue
                
            while (l < r):
                if (nums[i] + nums[l] + nums[r]) == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (l < r and nums[l-1] == nums[l]):
                        l += 1

                    r -= 1
                    while (l < r and nums[r+1] == nums[r]):
                        r -= 1
                elif (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                    while (l < r and nums[r+1] == nums[r]):
                        r -= 1
                    
                else: 
                    l += 1
                    while (l < r and nums[l-1] == nums[l]):
                        l += 1

        return output
                
        