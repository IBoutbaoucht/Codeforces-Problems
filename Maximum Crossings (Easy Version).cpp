#include <bits/stdc++.h>

using namespace std;
int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n ;
        vector<int> A(n);
        for (int i = 0; i < n; ++i) {
            cin >> A[i];
        }
        int r = 0 ;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if (A[j]<=A[i]){
                    r++ ;
                }
            }
        }
        
        cout << r << endl ;
        
       
    }

    return 0;
}
