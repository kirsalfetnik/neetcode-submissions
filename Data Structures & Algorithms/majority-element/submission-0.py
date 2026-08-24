class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        diction = {}

        for i in nums:
            diction.setdefault(str(i), 0)
            diction[str(i)] += 1

        max_key = max(diction, key=diction.get)
        max_key = int(max_key)
        return max_key