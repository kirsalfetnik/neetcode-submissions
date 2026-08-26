class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(0, len(nums)-1):
            l, r = i+1, len(nums)-1

            if (i > 0 and i < len(nums)-1):
                if nums[i-1] == nums[i]:
                    continue 

            while (l < r):
                if (nums[i] + nums[l] + nums[r]) == 0:
                    if [nums[i], nums[l], nums[r]] not in output:
                        output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
        
        return output
        