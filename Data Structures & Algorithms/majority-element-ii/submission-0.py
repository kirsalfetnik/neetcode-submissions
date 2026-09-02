class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = {}
        result = []

        for i in range(0, len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1

        for j in range(0, len(nums)):
            if hashMap[nums[j]] > (len(nums) / 3):
                if nums[j] not in result:
                    result.append(nums[j])

        return result 
        