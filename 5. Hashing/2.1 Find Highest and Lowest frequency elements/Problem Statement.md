# 2. Highest and Lowest Frequency Elements

## Problem

Given an array **_v_** of _**n**_ numbers, find and return the highest and lowest frequency elements.

If there are multiple elements having the highest frequency or lowest frequency, pick the smallest element.

**Example 1 :**

```
Input:
n=6
v=[1,2,3,1,1,4]

Output:
1 2

Explanation:
The element having the highest frequency is '1' and the frequency is 3. The elements with the lowest frequencies are '2', '3' and '4' and the frequency is 1. Since we need to pick the smallest element, we pick '2'. Hence, we return [1,2].
```

**Expected Time Complexity :**  
The expected time complexity is O(n), where n is the size of the array.

**Expected Space Complexity :**  
The expected time complexity is O(n), where n is the size of the array.

**Constraints :**  
2 <= n <= 10^4  
1 <= v[i] <= 10^9  
There are at least two distinct elements in the array.  
Time Limit: 1 sec
