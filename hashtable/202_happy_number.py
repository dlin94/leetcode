def isHappy(n):
    seen = set()
    while True:
        s = str(n)
        summed = sum([int(x)**2 for x in s])
        print(summed)
        if summed == 1:
            return True
        elif summed in seen:
            return False
        seen.add(summed)
        n = summed

print(isHappy(19))
print(isHappy(20))
print(isHappy(21))
print(isHappy(100))
print(isHappy(7))
