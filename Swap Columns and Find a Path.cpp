#include <bits/stdc++.h>

using namespace std;

int main() {

    int t ;
    cin >> t ;
    while(t--){
        int n;
        cin >> n;
        vector<int> A1(n) ;
        vector<int> A2(n) ;
        vector<int> T(n) ;
        int res = -2000000;
    
        for (int i = 0; i < n; i++) {
            cin >> A1[i] ;
        }
        for (int i = 0; i < n; i++) {
            cin >> A2[i] ;
        }
        for (int i = 0; i < n; i++) {
            T[i] = -min(A1[i],A2[i]);
        }
        int b = 2000000 ;
        for(int i=0;i<n;i++){
            b = min(b,T[i]) ;
        }
        int j ;
        for (int i = 0; i < n; i++) {
            if ( -min(A1[i],A2[i]) == b ){
                j = i ;
            }
        }
        res = A1[j]+A2[j] ;
        for(int i=0;i<n;i++){
            if (i != j){
                res+= max(A1[i],A2[i]) ;
            }
        }
        cout << res << endl;
    }
    return 0;
}
