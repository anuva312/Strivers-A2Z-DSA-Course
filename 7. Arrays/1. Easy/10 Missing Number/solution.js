// Time Complexity: O(nlogn)
// Space Complexity: O(1)
const missingNumberBruteForce = function (nums) {
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != i) {
      return i;
    }
  }
  return nums.length;
};

// Time Complexity: O(n)
// Space Complexity: O(n)
const missingNumber = function (nums) {
  let numsMap = {};
  for (const num of nums) {
    numsMap[num] = 1;
  }
  for (let i = 0; i < nums.length; i++) {
    if (!numsMap[i]) return i;
  }
  return nums.length;
};

// Time Complexity: O(n)
// Space Complexity: O(1)
const missingNumberOptimized = function (nums) {
  const arrayLength = nums.length;
  const expectedSum = (arrayLength * (arrayLength + 1)) / 2;
  const actualSum = nums.reduce((partialSum, a) => partialSum + a, 0);
  return expectedSum - actualSum;
};
