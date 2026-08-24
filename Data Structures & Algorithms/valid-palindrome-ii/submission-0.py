class Solution:
    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        counter = 2
        error = 0

        while (L < R):

            if (s[L] != s[R]):
                for i in range(2):
                    L, R = 0, len(s) - 1
                    error = 0

                    if i == 0:
                        while (L < R):
                            if (s[L] != s[R] and error < 1):
                                error += 1
                                L += 1
                                continue
                            elif (s[L] != s[R] and error >= 1):
                                counter -= 1
                                break

                            L += 1
                            R -= 1

                    if i == 1:
                        while (L < R):
                            if (s[L] != s[R] and error < 1):
                                error += 1
                                R -= 1
                                continue
                            elif (s[L] != s[R] and error >= 1):
                                counter -= 1
                                break

                            L += 1
                            R -= 1
                
            if (counter != 2):
                if counter == 0: 
                    return False
                elif counter == 1:
                    return True

            L += 1
            R -= 1
        
        return True
