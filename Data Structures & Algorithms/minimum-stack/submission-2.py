class MinStack:
    def __init__(self):
        # We initialize two arrays, minStack to keep track of the current min
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack == []:
            # Add anyway if minStack is empty
            self.minStack.append(val)
        else:
            # Add only if the top of minStack is greater than val
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        # This works because minStack will keep track of previous minimums
        # as well, and pop() will never be performend on an empty array (constr.)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Top of minStack will always be the minimum
        return self.minStack[-1]
