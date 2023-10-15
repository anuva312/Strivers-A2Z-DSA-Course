const twoSum = function (nums, target) {
  let pagesMap = {};
  let remainingPages = 0;
  for (let i = 0; i < nums.length; i++) {
    remainingPages = target - nums[i];
    pagesMap[remainingPages] = i;
  }
  for (let i = 0; i < nums.length; i++) {
    if (pagesMap[nums[i]] !== undefined && i !== pagesMap[nums[i]]) {
      return [pagesMap[nums[i]], i];
    }
  }
  return null;
};
