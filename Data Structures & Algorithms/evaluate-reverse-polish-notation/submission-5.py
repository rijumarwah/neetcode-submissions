class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]

        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                if i == "+":
                    res = stack[-2] + stack[-1]
                elif i == "-":
                    res = stack[-2] - stack[-1]
                elif i == "*":
                    res = stack[-2] * stack[-1]
                elif i == "/":
                    res = int(stack[-2] / stack[-1])

                stack.pop()
                stack.pop()
                stack.append(res)

        return stack[0]