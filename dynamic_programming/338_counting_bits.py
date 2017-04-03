#https://leetcode.com/problems/counting-bits/?tab=Description
from math import sqrt

def count_bits(num):
    count_ones = []
    for i in range(0, num+1):
        count = 0
        div = i
        while div > 0:
            if div % 2 == 1:
                count += 1
            div = div // 2
        count_ones.append(count)
    return(count_ones)

def count_bits_alt(num):
    count_ones = [0]
    offset = 1
    for i in range(1, num+1):
        if (offset * 2 == i):
            offset *= 2
        count_ones.append(count_ones[i-offset]+1)
    return count_ones
def print_bits(num):
    bits = []
    while num > 0:
        if num % 2 == 1:
            bits.insert(0, 1)
        else:
            bits.insert(0, 0)
        num = num // 2
    print(bits)

print_bits(52)
print_bits(100)

print(count_bits(16))
print(count_bits_alt(16))
