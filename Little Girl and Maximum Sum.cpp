#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main() {
    ll n, q;
    cin >> n >> q;
    vector<ll> A(n);
    for (ll i = 0; i < n; i++) {
        cin >> A[i];
    }
    vector<ll> Freq(n,0) ;
    for (ll i = 0; i < q; i++) {
        ll li, ri;
        cin >> li >> ri;
        Freq[li-1] += 1 ;
        if (ri < n) Freq[ri] -= 1 ;
    }
    for (ll i = 1; i < n; i++) {
        Freq[i] += Freq[i - 1];
    }
    sort(Freq.begin(),Freq.end()) ;
    sort(A.begin(),A.end()) ;
    ll s ;
    for(ll i=0;i<n;i++){
         s += A[i]*Freq[i] ;
    }
    cout << s << endl ;
    
    return 0;
}
