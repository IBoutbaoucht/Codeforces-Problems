
//          B. Equalize
//   time limit per test1 second
// memory limit per test256 megabytes


#include<bits/stdc++.h>
typedef long long ll ;

using namespace std;

int main(){
    int t ;
    cin >> t ;
    while(t--){
        ll n ;
        cin >> n ;
        set<ll> A ;
        ll v ;
        for(int i=0;i<n;i++){
            cin >> v ;
            A.insert(v) ;
        }
        
        std::vector<ll> V;
        ll m = 0;
        for(auto x:A){
            V.push_back(x);
            m++ ;
        }
        if(m == 1){
            cout << 1 << endl ;
            continue ;
        }
        ll res = 0 ;
        ll left = 0 ;
        ll right = 1 ;
        while(left < m && right < m ){
            while(right < m && V[right]-V[left]<n){
                right++ ;
            }
            res = max(right-left,res) ;
            left++ ;
        }
        cout << res << endl;
        
    }
    
    return 0;
}
