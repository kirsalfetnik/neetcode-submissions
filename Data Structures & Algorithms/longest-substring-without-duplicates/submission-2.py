class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        maxVal = 0

        l, r = 0, 0

        while l <= r and r < len(s):

            if s[r] not in hashSet:
                hashSet.add(s[r])
                maxVal = max(maxVal, len(hashSet))
                r += 1
            else: 
                hashSet.remove(s[l])
                l += 1
        
        return maxVal