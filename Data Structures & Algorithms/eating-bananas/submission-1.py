class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        bestRes = r

        while l <= r:
            mid = (l + r) // 2

            totalTime = 0
            for i in piles:
                totalTime += math.ceil(i / mid)
            if totalTime <= h:
                bestRes = min(bestRes, mid)
                r = mid - 1
            else:
                l = mid + 1
        return bestRes
