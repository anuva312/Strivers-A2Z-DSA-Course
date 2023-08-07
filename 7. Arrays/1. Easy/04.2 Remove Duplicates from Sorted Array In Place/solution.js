const removeDuplicates = function (nums) {
  let currentValue = nums[0];
  let duplicateCount = 0;
  const arrayLength = nums.length;
  for (i = 1; i < arrayLength; i++) {
    if (nums[i] == currentValue) {
      nums[i] = Infinity;
      duplicateCount++;
    } else {
      currentValue = nums[i];
    }
  }
  nums.sort((a, b) => a - b);
  nums.splice(arrayLength - duplicateCount, duplicateCount);
};
