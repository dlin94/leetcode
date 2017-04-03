from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()



    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        curr = None
        l = []
        while len(self.stack) > 0:
            curr = self.stack.popleft()
            if len(self.stack) >= 1:
                l.append(curr)
        print(l)
        for x in l:
            self.stack.append(x)
        return curr

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        curr = None
        l = []
        while len(self.stack) > 0:
            curr = self.stack.popleft()
            l.append(curr)
        for x in l:
            self.stack.append(x)
        return curr


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
