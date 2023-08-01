const rotate = function (nums, k) {
  const arrayLength = nums.length;
  const rotationsCount = k % arrayLength;
  for (let i = 0; i < rotationsCount; i++) {
    const temp = nums[arrayLength - 1];
    for (let index = arrayLength - 1; index >= 0; index--) {
      nums[index] = nums[index - 1];
    }
    nums[0] = temp;
  }
};
