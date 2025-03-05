#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> grid;
vector<vector<bool>> visited;

void color_rooms(int r, int c) {
    if (r < 0 || r >= n || c < 0 || c >= m || visited[r][c] || grid[r][c] == '#') {
        return;
    }
    visited[r][c] = true;
    color_rooms(r - 1, c);
    color_rooms(r + 1, c);
    color_rooms(r, c - 1);
    color_rooms(r, c + 1);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cin >> n >> m;
        cin.ignore();

        grid.clear();
        grid.resize(n);

        for (int i = 0; i < n; i++) {
            getline(cin, grid[i]);
        }

        bool done = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'B') {
                    if (i > 0) {
                        if (grid[i - 1][j] == '.') grid[i - 1][j] = '#';
                        else if (grid[i - 1][j] == 'G') done = true;
                    }
                    if (i < n - 1) {
                        if (grid[i + 1][j] == '.') grid[i + 1][j] = '#';
                        else if (grid[i + 1][j] == 'G') done = true;
                    }
                    if (j > 0) {
                        if (grid[i][j - 1] == '.') grid[i][j - 1] = '#';
                        else if (grid[i][j - 1] == 'G') done = true;
                    }
                    if (j < m - 1) {
                        if (grid[i][j + 1] == '.') grid[i][j + 1] = '#';
                        else if (grid[i][j + 1] == 'G') done = true;
                    }
                }
            }
        }

        if (done) {
            cout << "NO" << endl;
            continue;
        }
        visited.assign(n, vector<bool>(m, false));

        if (grid[n - 1][m - 1] != '#') {
            color_rooms(n - 1, m - 1);
        }

        for (int i = 0; i < n && !done; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'G' && !visited[i][j]) {
                    done = true; 
                    break;
                }
            }
        }
        if (done){cout<<"NO"<<endl;}
        else {cout<<"YES"<<endl;}
    }

    return 0;
}