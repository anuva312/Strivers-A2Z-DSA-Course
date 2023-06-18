# 8. Reverse A Number

## Problem 1

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**Example 1 :**

```
Input: x = 123
Output: 321
```

**Example 2 :**

```
Input: x = -123
Output: -321
```

**Example 3 :**

```
Input: x = 120
Output: 21
```

**Constraints:**  
-2^31 <= x <= 2^31 - 1

## Problem 2

Given a 32 bit number X, reverse its binary form and print the answer in decimal.

**Example 1 :**

```
Input:
X = 1

Output:
2147483648

Explanation:
Binary of 1 in 32 bits representation-
00000000000000000000000000000001
Reversing the binary form we get,
10000000000000000000000000000000,
whose decimal value is 2147483648.
```

**Task:**  
Complete the function reversedBits() which takes an Integer X as input and returns the answer.

**Expected Time Complexity:** O(log(X))  
**Expected Auxiliary Space:** O(1)

**Constraints:**  
0 <= X < 2^32
