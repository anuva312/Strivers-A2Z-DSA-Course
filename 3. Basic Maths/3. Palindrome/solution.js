// Time Complexity : O(log n)

// Space Compelxity : O(log n)
const isPalindrome = function (x) {
  if (x < 0) return false;
  let num = x + "";
  let left = 0;
  let right = num.length - 1;

  while (left < right) {
    if (num[left++] !== num[right--]) {
      return false;
    }
  }
  return true;
};

// Space Complexity : O(1)
const isPalindromeOptimized = function (x) {
  if (x < 0) return false;

  let reverse = 0;
  let original = x;

  while (x > 0) {
    const digit = x % 10;
    reverse = reverse * 10 + digit;
    x = Math.floor(x / 10);
  }
  return original === reverse;
};

const num = 1256521;
console.log(isPalindrome(num));
