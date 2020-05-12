class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.Min_stack = [float('inf')]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.Min_stack.append(min(x,self.Min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.Min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min_stack[-1]
