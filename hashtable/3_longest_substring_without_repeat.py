class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        current = 0
        ht = { } # store indices of current substring
        for i in range(0, len(s)):
            char = s[i]
            if char in ht:
                start = ht[char] + 1 # new index of start of current substring
                ht[char] = i
                for x in ht.keys():
                    if ht[x] < start:
                        del ht[x]
                current = i - start + 1
            else:
                ht[char] = i
                current += 1
                if current > longest:
                    longest = current

        return longest 
