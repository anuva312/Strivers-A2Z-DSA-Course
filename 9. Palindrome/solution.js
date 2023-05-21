const isPalindrome = function (x) {
  if (x < 0) return false;
  let num = x + "";
  let left = 0;
  let right = num.length - 1;

  console.log(num, left, right);
  while (left < right) {
    console.log(num[left], num[right]);
    if (num[left++] !== num[right--]) {
      return false;
    }
  }
  return true;
};

const num = 1256521;
console.log(isPalindrome(num));
