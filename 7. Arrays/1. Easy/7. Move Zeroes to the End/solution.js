const moveZeroes = function (nums) {
  const arrayLength = nums.length;
  let zeroCount = 0;
  let zeroPosition = -1;
  for (let i = 0; i < arrayLength; i++) {
    if (nums[i] === 0) {
      zeroCount++;
      if (zeroPosition === -1) {
        zeroPosition = i;
      }
    } else if (zeroPosition > -1) {
      let temp = nums[zeroPosition];
      nums[zeroPosition] = nums[i];
      nums[i] = temp;
      if (
        zeroPosition + 1 < arrayLength &&
        zeroPosition + 1 <= i &&
        nums[zeroPosition + 1] === 0
      ) {
        zeroPosition++;
      }
    }
  }
};
