class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        string = list(string)
        final = []
        for letter in string:
            if (letter.isalpha() or letter.isnumeric()):
                final.append(letter)
        
        L, R = 0, len(final) - 1

        while L < R:
            if final[L] != final[R]:
                return False
            L += 1
            R -= 1
        return True