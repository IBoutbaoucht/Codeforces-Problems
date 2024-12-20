#include <bits/stdc++.h>

using namespace std;
map<int,vector<int>> G ;
string S;
map<int,pair<int,int>> BlaxW ;

pair<int,int> BlackAndWhite(int vertice){
    pair<int,int> BW ;
    if (S[vertice-1] == 'B'){
        BW = {1,0} ;   
    }else {
        BW = {0,1} ;
    }
    if (G[vertice].empty()){
        return BW ;
    }
    for(auto child:G[vertice]){
        if (BlaxW.find(child) == BlaxW.end()){
            BlaxW[child] = BlackAndWhite(child) ;
        }
        BW.first += BlaxW[child].first ;
        BW.second += BlaxW[child].second ;
    }
    BlaxW[vertice] = BW ;
    return BW ;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        BlaxW.clear() ;
        G.clear() ;
        int n;
        cin >> n ;
        vector<int> A(n);
        map<int, pair<int,int>> BW;

        for (int i = 0; i < n-1; ++i) {
            cin >> A[i];
            G[A[i]].push_back(i+2) ;
        }
        cin >> S ;
        BlackAndWhite(1) ;
        int r = 0 ;
        for(int i=1;i<=n;i++){
            if(BlaxW[i].first == BlaxW[i].second){
                r++ ;
            }
        }
        cout << r << endl ;
       
    }

    return 0;
}
