/**
 *    author:  Chaitanya Brahmapurikar
 *    created: 05.04.2026 21:07:56
**/
#include <bits/stdc++.h>
using namespace std;

class dsu {
 public:
  vector<int> p, sz;
  int n;

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
    const int RUNS = 50;
    long long m = (long long)5 * N;

    long long mid = (long long)((N * log(N)) / 2.0);

    vector<long long> checkpoints;
    for (int d = -50; d <= 50; d += 10) {
        checkpoints.push_back(mid + d);
    }

    map<long long, map<int, double>> avg_map;
    map<long long, int> cnt_map;

    for (auto e : checkpoints) {
        avg_map[e] = map<int, double>();
        cnt_map[e] = 0;
    }

    for (int run = 0; run < RUNS; run++) {

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

            if (used[{u, v}]) {
                e--;
                continue;
            }

            used[{u, v}] = 1;
            D.unite(u, v);

            if (avg_map.count(e)) {

                unordered_map<int, int> comp_size;

                for (int i = 0; i < N; i++) {
                    int root = D.get(i);
                    comp_size[root]++;
                }

                map<int, int> freq;
                for (auto &it : comp_size) {
                    freq[it.second]++;
                }

                int cnt = cnt_map[e];

                set<int> all_sizes;
                for (auto &it : avg_map[e]) all_sizes.insert(it.first);
                for (auto &it : freq) all_sizes.insert(it.first);

                for (int sz : all_sizes) {
                    double old_avg = avg_map[e][sz];
                    int val = freq.count(sz) ? freq[sz] : 0;

                    avg_map[e][sz] = (old_avg * cnt + val) / (cnt + 1);
                }

                cnt_map[e]++;
            }
        }
    }

    for (auto &cp : checkpoints) {
        cout << "e = " << cp << "\n";
        cout << "Average component sizes:\n";

        for (auto &it : avg_map[cp]) {
            cout << it.first << " : " << fixed << setprecision(2) << it.second << "\n";
        }

        cout << "-----------------------------\n";
    }

    return 0;
}
