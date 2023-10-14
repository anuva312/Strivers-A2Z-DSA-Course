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


print(getLongestSubarray([1, 2, 4, 2, -3, 2], 4))
