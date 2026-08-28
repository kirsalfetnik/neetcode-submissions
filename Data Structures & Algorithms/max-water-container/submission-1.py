class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l, r = 0, len(heights)-1

        while (l < r):
            compute = (r - l) * min(heights[l], heights[r])
            if compute > maxWater:
                maxWater = compute
            if (heights[l] <= heights[r]):
                l += 1
            else: r -= 1
        
        return maxWater
