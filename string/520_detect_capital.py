def detect_capital(word):
    # If first letter lower, then the rest must be lower
    if word[0].islower():
        return word == word.lower()
    # First letter upper
    else:
        # If word is all upper case, then it passes
        if word == word.upper():
            return True
        # Else, the rest of the word must be all lower
        else:
            return word[1:] == word[1:].lower()

print(detect_capital("USA"))
print(detect_capital("FlaG"))
print(detect_capital("test"))
print(detect_capital("tesT"))
