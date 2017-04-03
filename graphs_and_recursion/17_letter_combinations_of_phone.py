class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        if not digits:
            return ans

        d = { '1':['*'],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'], \
              '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'], \
              '8':['t','u','v'],'9':['w','x','y','z']}
        self.generate(digits, "", 0, d, ans)
        return ans

    def generate(self, digits, s, i, d, ans):
        if i == len(digits):
            ans.append(s)
        else:
            for char in d[digits[i]]:
                self.generate(digits, s+char, i+1, d, ans)
