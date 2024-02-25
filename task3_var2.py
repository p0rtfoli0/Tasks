def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i] + max_ending_here:
            s = i
            max_ending_here = arr[i]
        else:
            max_ending_here = arr[i] + max_ending_here

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return arr[start:end+1]
