const reverseArray = function (nums, startingPosition, endingPosition) {
  while (startingPosition < endingPosition) {
    let temp = nums[startingPosition];
    nums[startingPosition] = nums[endingPosition];
    nums[endingPosition] = temp;
    startingPosition++;
    endingPosition--;
  }
};

function rotate(arr, k) {
  let arrayLength = arr.length;
  const rotationCount = arrayLength - k;
  if (rotationCount === arrayLength) return;
  reverseArray(arr, 0, arrayLength - 1);
  reverseArray(arr, 0, (rotationCount - 1) % arrayLength);
  reverseArray(arr, rotationCount % arrayLength, arrayLength - 1);
}
