# DFS (recursive), backtracking, stack, string
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.tryCombo("", n, n, n, ans)
        return ans

    # Use recursion and backtracking to test all possible combinations
    def tryCombo(self, s, n, opened, closed, ans):
        print(s)
        if len(s) == 2*n:
            if self.check(s):
                ans.append(s)
        else:
            if self.check(s):
                if opened:
                    self.tryCombo(s + "(", n, opened - 1, closed, ans)

                if closed:
                    self.tryCombo(s + ")", n, opened, closed - 1, ans)

    # Check if a combination is valid
    def check(self, s):
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
        return True
