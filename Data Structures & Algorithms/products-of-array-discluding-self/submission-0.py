class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        total_mul = 1
        no_nulls_mul = 1
        null_count = 0

        if ((len(nums) == 1) and (0 in nums)):
            answer = [0]
            return answer
        
        for j in nums:
            if j != 0:
                no_nulls_mul *= j
            else:
                null_count += 1

        if null_count > 1:
            return answer

        for i in nums:
            total_mul *= i

        for i in range(0, len(nums)):
            if nums[i] != 0:
                answer[i] = int(nums[i]**(-1) * total_mul)
            else:
                answer[i] = no_nulls_mul
        
        return answer
        