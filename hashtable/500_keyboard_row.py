# https://leetcode.com/problems/keyboard-row/?tab=Description
def findWords(words):
    return_list = []
    one, two, three = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    for word in words:
        lword = word.lower()
        if set(lword).issubset(one) or set(lword).issubset(two) or set(lword).issubset(three):
            return_list.append(word)
        #if len([ x for x in word if x in ]) == len(word):
        #    return_list.append(word)
    return return_list

print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
