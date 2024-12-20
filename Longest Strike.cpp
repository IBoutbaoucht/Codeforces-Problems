#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> A(n);
        map<int, int> freq;

        // Read input and calculate frequencies
        for (int i = 0; i < n; ++i) {
            cin >> A[i];
            freq[A[i]]++;
        }

        int l = numeric_limits<int>::max();
        int r = numeric_limits<int>::min();
        set<int> visited;

        // Process each element in the frequency map
        for (const auto& [e, count] : freq) {
            if (count >= k && visited.find(e) == visited.end()) {
                int le = e, re = e;

                // Expand to the right
                while (freq[re] >= k) {
                    visited.insert(re);
                    re++;
                }

                // Expand to the left
                while (freq[le] >= k) {
                    le--;
                    visited.insert(le);
                }

                // Check if the current range is better
                if (re - le > r - l) {
                    r = re;
                    l = le;
                }
            }
        }

        if (l == numeric_limits<int>::max()) {
            cout << -1 << endl;
        } else {
            cout << l + 1 << " " << r - 1 << endl;
        }
    }

    return 0;
}
