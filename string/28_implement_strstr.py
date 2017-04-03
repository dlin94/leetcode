class Solution(object):
    # Bruteforce O(mn) solution
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        m, n = len(haystack), len(needle)
        for i in range(0, m-n+1):
            for j in range(0, n):
                if needle[j] != haystack[i+j]:
                    break
                if j == n - 1:
                    return i
        return -1
