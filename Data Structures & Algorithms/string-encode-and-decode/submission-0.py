class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ''

        for word in strs:
            tmp = ''
            for letter in word:
                l = str(ord(letter) - ord('a'))
                tmp += l
                tmp += '_'
            enc += tmp
            enc += '*'

        return enc
            

    def decode(self, s: str) -> List[str]:
        final = []
        pointer = 0
        number = ''
        tmp = ''

        while pointer < len(s):
            if (s[pointer] != '_' and s[pointer] != '*'):
                #number += chr(ord('a') + ord(s[pointer]))
                number += s[pointer]
                pointer += 1
            elif s[pointer] == '_':
                tmp += chr(ord('a') + int(number))
                number = ''
                pointer += 1
            elif s[pointer] == '*':
                final.append(tmp)
                tmp = ''
                pointer += 1
        return final

            
