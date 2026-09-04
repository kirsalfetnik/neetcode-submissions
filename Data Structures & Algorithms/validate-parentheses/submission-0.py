class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(0,len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if s[i] == "]" and len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                elif s[i] == ")" and len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                elif s[i] == "}" and len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False