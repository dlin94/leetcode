def find_duplicates(nums):
    d = {}
    for i in range (0, len(nums)):
        if nums[i] in d:
            d[nums[i]] += 1
        else:
            d[nums[i]] = 1
    return [x for x in d if d[x] == 2]

# For this to work, 1 <= nums[i] <= len(nums)
# Example array: [3, 4, 2, 3, 2]
# It works like this: We note that we have seen a number by making the num at the
# index abs(x) -1 negative. So if we0 see 3 @ i=0, then we make nums[2] = -2. If we encounter
# 3 again, then it will go to nums[2], see that the value is negative, and put 3 in the
# results list.

def find_duplicates_alt(nums):
    res = []
    for x in nums:
        print(x)
        if nums[abs(x)-1] < 0: # Saw abs(x) again; put it in result
            res.append(abs(x))
        else: # Indicate that we have seen abs(x)
            nums[abs(x)-1] *= -1
    return res

print(find_duplicates([4,3,2,7,8,2,3,1]))
print(find_duplicates_alt([3,4,2,3,2]))

list_ = [1]
#print(list_[1])
