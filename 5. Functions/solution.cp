#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> passedBy(int a, int &b) {
        vector<int> arr;
        b=b+2;
        arr.push_back(a+1);
        arr.push_back(b);
        return arr;
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a, b;
        cin >> a >> b;
        Solution obj;
        vector<int> ans = obj.passedBy(a, b);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}