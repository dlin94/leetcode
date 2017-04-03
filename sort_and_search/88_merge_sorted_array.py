def merge(nums1, m, nums2, n):
    if n == 0:
        return
    elif m == 0:
        for i in range(0, n):
            nums1[i] = nums2[i]

    i = 0
    j = 0
    k = 0 # keep track of index of modified nums1
    while i < m and j < n:
        if nums2[j] < nums1[k]:
            nums1.insert(k, nums2[j])
            nums1.pop()
            j += 1
            print("here")
        else:
            i += 1
        k += 1
    while j < n:
        idx = -(n-j)
        print(idx, j, n, nums2[j])
        nums1[idx] = nums2[j]
        j += 1

    print(nums1)

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
