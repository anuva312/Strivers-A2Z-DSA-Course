// Time Complexity: O(n log n)
// Space Complexity: O(1)
// Auxiliary Space: O(1)

const maxFrequency = function (nums, k) {
  nums.sort((a, b) => a - b);
  let start = 0;
  let sum = 0;
  let maxPossibleFrequency = 0;
  for (let end = 0; end < nums.length; end++) {
    sum += nums[end];
    while ((end - start + 1) * nums[end] - sum > k) {
      sum -= nums[start];
      start++;
    }
    maxPossibleFrequency = Math.max(maxPossibleFrequency, end - start + 1);
  }
  return maxPossibleFrequency;
};
