def isValid(s):
    old_len = len(s)
    while len(s) > 0:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
        if len(s) == old_len:
            return False
        old_len = len(s)
    return True
    
def isValid_alt(self, s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

print(isValid("([)]"))
