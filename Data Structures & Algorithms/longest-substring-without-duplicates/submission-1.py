class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hashSet = set()
        maxCounter = 0 
        currCounter = 0

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
           
        hashSet.add(s[l])
        length = len(hashSet)
        
        while r < len(s) and l <= r:
            if length != (r - l + 1):
                hashSet.remove(s[l])
                l += 1
                hashSet.add(s[r])
                hashSet.add(s[l])
            elif length == (r - l + 1):
                r += 1
                if r < len(s):
                    hashSet.add(s[r])
            length = len(hashSet)
            maxCounter = max(maxCounter, length)

        return maxCounter


