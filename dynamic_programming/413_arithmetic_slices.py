def num_slices(A):
    ans = 0 # number of slices
    diff_count = 0 # this is incremented if the current diff is the same as the prev one
    old_diff = None # this keeps track of the previous diff
    for i in range(1, len(A)): # start @ i = 1
        # Get the curr diff, check if it is equal to the previous diff.
        # Increment the diff_count if so.
        curr_diff = A[i] - A[i-1]
        if curr_diff == old_diff:
            diff_count += 1
            # If we have at least two of the same diffs in a row, then increment
            # the answer by diff_count - 1. Why diff_count - 1? Because we need
            # to count the new arithmetic slices created by checking the newest
            # number. Each of these slices will end at the most recent number
            # (since we've already counted all the inner slices), so we simply
            # up to the 2 positions away from the current index position starting
            # at the index from which we began the diff_count. This is diff_count-2.
            # Example: We have a slice [1,2,3,4,5]. We've already counted all the slices
            # in [1,2,3,4], so count all the new slices created from adding 5:
            # [1,2,3,4,5], [2,3,4,5], [3,4,5]. 3 slices, or (diff_count = 4) - 1
            if diff_count >= 2:
                ans += diff_count - 1
        else:
            diff_count = 1

        old_diff = curr_diff
    return ans
