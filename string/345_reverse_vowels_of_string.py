class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a','e','i','o','u', 'A', 'E','I','O','U'])
        print(vowels)
        l = list(s)
        i = 0
        j = len(l) - 1
        while i < j:
            if l[i] in vowels and l[j] in vowels:
                l[i], l[j] = l[j], l[i]
                print("both in vowels")
                i += 1
                j -= 1
            elif l[j] in vowels: # but not s[i], so stay on j and increment i
                print(l[j], "j in vowels")
                i += 1
            elif l[i] in vowels: # but not s[j], so stay on i and increment i
                j -= 1
            else: # neither are vowels
                i += 1
                j -= 1
        return "".join(l)
