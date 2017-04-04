class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(0, numRows):
            ans.append([1])
            if i > 0:
                if i > 1:
                    for j in range (0, len(ans[i-1])-1):
                        ans[i].append(ans[i-1][j] + ans[i-1][j+1])
                ans[i].append(1)
        return ans
