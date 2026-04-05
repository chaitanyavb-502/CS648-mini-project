/**
 *    author:  Chaitanya Brahmapurikar
**/
#include <bits/stdc++.h>
using namespace std;

class dsu {
 public:
  vector<int> p, sz;
  int n;
  int mx_sz = 1;

  dsu(int _n) : n(_n) {
    p.resize(n);
    sz.resize(n, 1);
    iota(p.begin(), p.end(), 0);
  }

  int get(int x) {
    return (x == p[x] ? x : (p[x] = get(p[x])));
  }

  bool unite(int x, int y) {
    x = get(x);
    y = get(y);
    if (x != y) {
      p[x] = y;
      sz[y] += sz[x];
      mx_sz = max(mx_sz, sz[y]);
      return true;
    }
    return false;
  }
};

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

int rand_int(int l, int r) {
    uniform_int_distribution<int> dist(l, r);
    return dist(rng);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const int N = 1000;
    const int RUNS = 10;
    long long m = (long long)5 * N;

    for (int run = 0; run < RUNS; run++) {
        dsu D(N);
        map<pair<int, int>, int> used;

        int connected_at = -1;

        for (long long e = 1; e <= m; e++) {
            int u = rand_int(0, N - 1);
            int v = rand_int(0, N - 1);

            if (u == v) {
                e--;
                continue;
            }
            if (u > v) swap(u, v);

            if (used[{u, v}]) {
                e--;
                continue;
            }

            used[{u, v}] = 1;
            D.unite(u, v);

            if (D.mx_sz == N && connected_at == -1) {
                connected_at = e;
            }
            cout << run << " " << e << " " << D.mx_sz << "\n";
        }
        cout << "# CONNECTED " << run << " " << connected_at << "\n";
    }
    return 0;
}
