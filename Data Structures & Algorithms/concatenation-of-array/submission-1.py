class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        final_array = []

        for i in range(0,len(nums)):
            final_array.append(nums[i])

        for i in range(len(nums)):
            final_array.append(nums[i])

        return final_array
        