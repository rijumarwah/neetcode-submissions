class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        opening = ('(', '[', '{')
        closing = (')', ']', '}')

        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        
                