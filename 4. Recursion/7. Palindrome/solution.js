// Time Complexity: O(N)
// Space Complexity: O(N)
// Auxiliary Space: O(N)

// The below code can correctly check if a given string is a palindrome or not. However, both these approaches have higher space complexity, and for very long strings, it may lead to stack overflow errors.

class Solution {
  isPalindrome(S) {
    const stringLength = S.length;
    if (stringLength <= 1) {
      return 1;
    }
    if (S.charAt(0) === S.charAt(stringLength - 1)) {
      return this.isPalindrome(S.slice(1, stringLength - 1));
    } else return 0;
  }
}

// Using tail recursion

class Solution {
  isPalindrome(S) {
    return this.isPalindromeTailRecursive(S, 1);
  }

  isPalindromeTailRecursive(S, accumulator) {
    const stringLength = S.length;
    if (stringLength <= 1) {
      return accumulator;
    }
    if (S.charAt(0) === S.charAt(stringLength - 1)) {
      return this.isPalindromeTailRecursive(
        S.slice(1, stringLength - 1),
        accumulator
      );
    } else {
      return 0;
    }
  }
}
