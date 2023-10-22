// Brute Force Solution
// Time Complexity : O(n)
// Space Complexity : O(1)
// Two Pass Approach

const sortColors = function (nums) {
  let zeroesCount = 0;
  let onesCount = 0;
  let twosCount = 0;
  for (const num of nums) {
    if (num === 0) zeroesCount++;
    else if (num === 1) onesCount++;
    else twosCount++;
  }
  for (let i = 0; i < nums.length; i++) {
    if (zeroesCount) {
      nums[i] = 0;
      zeroesCount--;
    } else if (onesCount) {
      nums[i] = 1;
      onesCount--;
    } else if (twosCount) {
      nums[i] = 2;
      twosCount--;
    }
  }
};

// Dutch National Flag Algorithm
// Time Complexity : O(n)
// Space Complexity : O(1)
// One Pass Approach

const sortColorsOptimized = function (nums) {
  let low = 0;
  let mid = 0;
  let high = nums.length - 1;
  let temp = 0;
  while (mid <= high) {
    if (nums[mid] === 0) {
      temp = nums[low];
      nums[low] = nums[mid];
      nums[mid] = temp;
      low++;
      mid++;
    } else if (nums[mid] === 1) {
      mid++;
    } else {
      temp = nums[high];
      nums[high] = nums[mid];
      nums[mid] = temp;
      high--;
    }
  }
};
