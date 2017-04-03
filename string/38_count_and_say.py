def countAndSay(n):
    curr = str("1")
    for i in range(2, n+1):
        sequence = ""
        j = 0
        while j < len(curr):
            count = 0
            num = curr[j]
            while True:
                if j >= len(curr):
                    break
                elif curr[j] == num:
                    count += 1
                    j += 1
                else:
                    break
            print(i, j, sequence)
            sequence += str(count) + num

        curr = sequence
    return curr

print(countAndSay(5))
