#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main() {
    ll n, m, k;
    cin >> n >> m >> k;
    
    vector<ll> A(n, 0);
    vector<ll> B(n + 1, 0);  
    vector<ll> C(m + 1, 0); 
    
    for (ll i = 0; i < n; i++) {
        cin >> A[i];
    }
    
    map<ll, vector<ll>> Operations;
    for (ll i = 0; i < m; i++) {
        ll li, ri, di;
        cin >> li >> ri >> di;
        Operations[i + 1] = {li, ri, di};
    }
    
    for (ll i = 0; i < k; i++) {
        ll xi, yi;
        cin >> xi >> yi;
        
        C[xi - 1] += 1;  
        if (yi < m) C[yi] -= 1;  
    }
    
    for (ll i = 1; i < m; i++) {
        C[i] += C[i - 1];
    }
    
    for (ll i = 0; i < m; i++) {
        ll li = Operations[i + 1][0];
        ll ri = Operations[i + 1][1];
        ll di = Operations[i + 1][2];
        
        ll delta = di * C[i];
        B[li - 1] += delta;
        if (ri < n) B[ri] -= delta;
    }
    
    for (ll i = 1; i < n; i++) {
        B[i] += B[i - 1];
    }
    
    for (ll i = 0; i < n; i++) {
        A[i] += B[i];
    }
    
    for (ll i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    cout << endl;
    
    return 0;
}
