#include <bits/stdc++.h>
using namespace std;

void isPrime(int n) {
    string result = "Yes";
    if(n<2){
        result = "No";
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if(n%i == 0){
            result =  "No";
            break;
        }
    }
cout << result << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        isPrime(n);
    }
    return 0;
}