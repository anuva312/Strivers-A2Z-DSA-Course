const reverseArray = function (nums, startingPosition, endingPosition) {
  while (startingPosition < endingPosition) {
    let temp = nums[startingPosition];
    nums[startingPosition] = nums[endingPosition];
    nums[endingPosition] = temp;
    startingPosition++;
    endingPosition--;
  }
};

const rotate = function (nums, k) {
  let arrayLength = nums.length;
  if (k === arrayLength) return;
  reverseArray(nums, 0, arrayLength - 1);
  reverseArray(nums, 0, (k - 1) % arrayLength);
  reverseArray(nums, k % arrayLength, arrayLength - 1);
};
