/**
 *    author:  Chaitanya Brahmapurikar
 *    created: 02.04.2026 17:48:38
**/
#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#include "debug.h"
#else
#define debug(...)
#define debugArr(...)
#endif

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

  inline int get(int x) {
    return (x == p[x] ? x : (p[x] = get(p[x])));
  }

  inline bool unite(int x, int y) {
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
    long long m = (long long)5 * N;

    dsu D(N);
    map<pair<int, int>, int> used;
    for (long long e = 1; e <= m; e++) {
        int u = rand_int(0, N - 1);
        int v = rand_int(0, N - 1);
        if (u == v) {
            e--; 
            continue;
        }
        if (u > v) swap(u, v);
        if (used[make_pair(u, v)]) {
            e--;
            continue;
        }
        used[make_pair(u, v)] = 1;
        D.unite(u, v);
        //if (e == N / 2 || e == 2 * N) {
        //    cout << "e = " << e << ' ' << "mx_sz = " << D.mx_sz << '\n';
        //}
        cout << e << ' ' << D.mx_sz << '\n';
    }
    return 0;
}
