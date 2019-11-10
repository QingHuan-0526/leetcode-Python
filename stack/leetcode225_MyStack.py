"""
leetcode 225
用队列实现栈
"""
import collections

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.pop())
        return self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        top = self.stack.pop()
        self.stack.append(top)
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.pop())
        return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.stack

