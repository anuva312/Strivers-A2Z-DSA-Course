def longestSubarrayWithSumK(a: [int], k: int) -> int:
    longest_subarray_length = 0
    start = 0
    sum = 0
    for end in range(len(a)):
        if start > end:
            continue
        sum += a[end]
        while sum > k:
            sum -= a[start]
            start += 1
        if sum == k:
            subarray_length = end - start + 1
            if subarray_length > longest_subarray_length:
                longest_subarray_length = subarray_length

    return longest_subarray_length
