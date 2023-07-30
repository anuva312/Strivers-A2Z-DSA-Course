// Time Complexity: O(N)
// Space Complexity: O(P)
// Auxiliary Space: O(P)
class Solution {
  frequencyCount(arr, N, P) {
    const countMap = {};
    for (const element of arr) {
      if (countMap[element]) {
        countMap[element]++;
      } else {
        countMap[element] = 1;
      }
    }
    for (let i = 0; i < N; i++) {
      if (countMap[i + 1]) {
        arr[i] = countMap[i + 1];
      } else {
        arr[i] = 0;
      }
    }
  }
}
