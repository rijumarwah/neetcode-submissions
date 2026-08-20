class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # If stack is non-empty and check if today's temp resolves
            # the temp at top of stack. If it does, remove it, and add
            # to result.
            # If no result, result for that day/index will stay 0.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            # Add the day to stack
            stack.append(i)

        return result