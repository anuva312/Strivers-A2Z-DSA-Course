//  Time complexity : O(log n)
//  Space complexity : O(1)

function reverseBits(X) {
  let binaryNum = X.toString(2).padStart(32, "0");
  let binaryNumReversed = binaryNum.split("").reverse().join("");
  return parseInt(binaryNumReversed, 2);
}
