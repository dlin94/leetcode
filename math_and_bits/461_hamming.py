def hamming_distance(x, y):
    x_bits = _get_bits(x)
    y_bits = _get_bits(y)

    if len(x_bits) > len(y_bits):
        y_bits = (len(x_bits)-len(y_bits)) * [0] + y_bits
    else:
        x_bits = (len(y_bits)-len(x_bits)) * [0] + x_bits

    count = 0
    for i in range(len(x_bits)-1, -1, -1):
        if x_bits[i] != y_bits[i]:
            count += 1
    return count

def _get_bits(num):
    bits = []
    while num > 0:
        if num % 2 == 1:
            bits.insert(0, 1)
        else:
            bits.insert(0, 0)
        num = num // 2
    return bits

# XOR x and y, find the binary string, which will contain ones only at the positions
# in which x and y's binary forms differ. Count the ones, and return this count.
def hamming_distance_alt(x, y):
    return bin(x^y).count('1')

print(hamming_distance(1,4))
print(hamming_distance_alt(1,4))
