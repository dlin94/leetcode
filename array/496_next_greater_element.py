def next_greater_element(nums1, nums2):
    max_num = 0
    return_list = []
    for i in range(0, len(nums1)):
        next_greater = -1
        for j in range(0, len(nums2)):
            if nums2[j] == nums1[i]:
                for k in range (j+1, len(nums2)):
                    if nums2[k] > nums2[j]:
                        next_greater = nums2[k]
                        break
                break
        return_list.append(next_greater)
    return return_list

def next_greater_element_alt(nums1, nums2):
    d = {}
    st = [] # stack 
    ans = [] # stores our answer

    #
    for x in nums2:
        while len(st) and st[-1] < x:
            d[st.pop()] = x
        st.append(x)

    for x in nums1:
        ans.append(d.get(x, -1))

    return ans

print(next_greater_element([2,4], [1,2,3,4]))
print(next_greater_element_alt([2,4], [1,2,3,4]))
