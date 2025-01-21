#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <cstring>

using namespace std;

const int MAX_M = 10;
const int MAX_MASK = 1 << MAX_M;
short popcount[MAX_MASK];

void precompute_popcount() {
    for (int s = 0; s < MAX_MASK; s++) {
        popcount[s] = __builtin_popcount(s);
    }
}

struct IncItem {
    int v, i, c;
    IncItem(int v, int i, int c) : v(v), i(i), c(c) {}
    bool operator<(const IncItem& other) const {
        return v < other.v;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    precompute_popcount();

    int t;
    cin >> t;
    
    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;
        
        vector<long long> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }

        vector<int> B(m);
        for (int j = 0; j < m; j++) {
            cin >> B[j];
        }

        vector<int> inter(1 << m, (1 << 30) - 1);
        for (int s = 1; s < (1 << m); s++) {
            int maskVal = (1 << 30) - 1;
            for (int bit = 0; bit < m; bit++) {
                if ((s >> bit) & 1) {
                    maskVal &= B[bit];
                }
            }
            inter[s] = maskVal;
        }

        const int INF = INT_MAX;
        vector<vector<int>> minVal(n, vector<int>(m + 1, INF));
        for (int i = 0; i < n; i++) {
            if (A[i] == 0) {
                fill(minVal[i].begin(), minVal[i].end(), 0);
                continue;
            }

            vector<int> bestValForC(m + 1, INF);
            long long ai = A[i];
            bestValForC[0] = ai & inter[0];
            
            for (int s = 1; s < (1 << m); s++) {
                int cSet = popcount[s];
                int candidate = ai & inter[s];
                if (candidate < bestValForC[cSet]) {
                    bestValForC[cSet] = candidate;
                }
            }
            for (int c = 0; c <= m; c++) {
                minVal[i][c] = bestValForC[c];
            }
        }

        vector<vector<int>> improvement(n, vector<int>(m + 1, 0));
        vector<vector<int>> inc(n, vector<int>(m, 0));

        for (int i = 0; i < n; i++) {
            long long ai = A[i];
            for (int c = 0; c <= m; c++) {
                improvement[i][c] = ai - minVal[i][c];
            }
            for (int c = 0; c < m; c++) {
                inc[i][c] = improvement[i][c + 1] - improvement[i][c];
            }
        }

        priority_queue<IncItem> pq;
        for (int i = 0; i < n; i++) {
            if (m > 0) {
                pq.push(IncItem(inc[i][0], i, 0));
            }
        }

        long long totalImprovement = 0;
        int usedOps = 0;
        while (usedOps < k && !pq.empty()) {
            IncItem top = pq.top();
            pq.pop();

            if (top.v <= 0) {
                break;
            }

            totalImprovement += top.v;
            usedOps++;

            int idx = top.i;
            int cOld = top.c;
            int cNew = cOld + 1;
            if (cNew < m) {
                pq.push(IncItem(inc[idx][cNew], idx, cNew));
            }
        }

        long long sumA = 0;
        for (long long x : A) {
            sumA += x;
        }

        cout << sumA - totalImprovement << endl;
    }

    return 0;
}
