const findMaxConsecutiveOnes = function (nums) {
  let maxConsecutiveOnes = 0;
  let currentConsecutiveOnes = 0;
  for (const item of nums) {
    if (item) {
      currentConsecutiveOnes++;
    } else {
      if (currentConsecutiveOnes > maxConsecutiveOnes) {
        maxConsecutiveOnes = currentConsecutiveOnes;
      }
      currentConsecutiveOnes = 0;
    }
  }
  if (currentConsecutiveOnes > maxConsecutiveOnes) {
    maxConsecutiveOnes = currentConsecutiveOnes;
  }
  return maxConsecutiveOnes;
};
