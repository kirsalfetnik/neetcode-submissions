class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        result = []

        for i in range(0, len(nums)):
            if nums[i] in res:
                res[nums[i]] += 1
            else: 
                res[nums[i]] = 1

        asc = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}

        for j in range(k):
            last_key = list(asc)[-1]
            asc.pop(last_key)
            result.append(last_key)
        
        return result