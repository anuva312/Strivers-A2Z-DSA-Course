// Brute Force Solution

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
