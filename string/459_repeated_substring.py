def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    match = False
    substring = s[0]
    idx = 0
    i = 1
    failed = set()
    while i < len(s):
        if match:
            if s[i] == substring[idx]:
                idx = (idx + 1) % len(substring)
            else:
                match = False
                idx = 0
                failed.add(substring)
                for k in range(len(substring)+1, len(s)):
                    substring = s[0:len(substring)+1]
                    if substring not in failed:
                        break
                #substring = s[0:len(substring)+1] # next candidate
                i = len(substring)-1
        else:
            if s[i] != substring[0]:
                substring += s[i]
            else:
                idx = (idx + 1) % len(substring)
                match = True

        if len(substring) > len(s)/2:
            return False
        i += 1
    return idx == 0 and match

# If the string is made up of substrings, then the first char in s is the first char
# in the substring, and the last char in s is the last char in the substring.
# Append s to s and take out the first and last chars. If s is indeed made up of
# substrings, then s+s is also made up of the same substring. So if we take out the
# first and last chars of s+s, making it ss, then we should still be able to find s in ss.
# If s is not made up of substrings, then taking out the first and last chars will make it
# impossible to find s.
def repeatedSubstringPattern_alt(s):
    ss = (s+s)[1:-1]

    return ss.find(s) != -1

print(repeatedSubstringPattern("abcdefghiabcdefghiabcdefghiabcdefghiabcdefghiabcdefghiabcdefghiabcdefghiabcdefghiabcdefghi"))
