"""
leetcode 155
最小栈
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        top = self.data.pop()
        if top == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]