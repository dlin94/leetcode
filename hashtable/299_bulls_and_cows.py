from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        c = Counter(secret)
        bulls = 0
        cows = 0
        # Go through each char in guess and check if it is in c
        for i in range(0, len(guess)):
            if guess[i] in c:
                if guess[i] == secret[i]:
                    bulls += 1

                    if c[guess[i]] > 0:
                        c[guess[i]] -= 1
                    else:
                        cows -= 1
                else:
                    if c[guess[i]] > 0:
                        cows += 1
                        c[guess[i]] -= 1

        return str(bulls)+"A"+str(cows)+"B"
