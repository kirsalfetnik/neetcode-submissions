class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L, R = 0, 0
        final = ''
        while (L < len(word1) or R < len(word2)):
            if (L < len(word1)):
                final += word1[L]
                L += 1
            if (R < len(word2)):
                final += word2[R]
                R += 1
        return final