

//       C. Number of Pairs
//   time limit per test2 seconds
// memory limit per test256 megabytes


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;



int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        int n, l, r;
    cin >> n >> l >> r;
    vector<int> A(n);
    
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    
    sort(A.begin(), A.end());
    ll ans = 0;
    
    for (int i = 0; i < n; i++) {
        // Find the smallest j such that A[i] + A[j] >= l and j > i
        int left = lower_bound(A.begin() + i + 1, A.end(), l - A[i]) - A.begin();
        
        // Find the largest j such that A[i] + A[j] <= r and j > i
        int right = upper_bound(A.begin() + i + 1, A.end(), r - A[i]) - A.begin() - 1;
        
        // Count valid pairs
        if (left <= right) {
            ans += (right - left + 1);
        }
    }
    
    cout << ans << "\n";
    }
    
    return 0;
}
