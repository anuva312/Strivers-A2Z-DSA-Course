const check = function (nums) {
  rotatedCount = 0;
  for (i = 1; i < nums.length; i++) {
    if (nums[i - 1] > nums[i]) {
      rotatedCount++;
      if (
        rotatedCount > 1 ||
        (rotatedCount && nums[0] < nums[nums.length - 1])
      ) {
        return false;
      }
    }
  }
  return true;
};
