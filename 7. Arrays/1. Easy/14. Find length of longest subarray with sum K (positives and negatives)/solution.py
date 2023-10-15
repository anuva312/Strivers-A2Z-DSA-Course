def getLongestSubarray(nums, k):
    longest_subarray_length = 0
    array_length = len(nums)
    for i in range(array_length):
        current_sum = 0
        for j in range(i, array_length):
            current_sum += nums[j]
            if current_sum == k:
                current_length = j - i + 1
                if current_length > longest_subarray_length:
                    longest_subarray_length = current_length
    return longest_subarray_length


def getLongestSubarrayOptimized(nums, k):
    array_length = len(nums)

    previous_sums_map = {}
    sum = 0
    max_length = 0
    for i in range(array_length):
        sum += nums[i]
        if sum == k:
            max_length = max(max_length, i + 1)
        rem = sum - k

        if rem in previous_sums_map:
            current_length = i - previous_sums_map[rem]
            max_length = max(max_length, current_length)

        if sum not in previous_sums_map:
            previous_sums_map[sum] = i

    return max_length
