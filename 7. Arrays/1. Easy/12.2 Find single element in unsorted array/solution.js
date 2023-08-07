// Hint : XOR of two equal numbers is 0
const singleNumber = function (nums) {
  let result = 0;
  for (const element of nums) {
    result = result ^ element;
  }
  return result;
};
