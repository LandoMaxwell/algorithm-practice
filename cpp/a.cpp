// 斜堆插入序列重构算法 (C++)
// 来源：cpp-algorithms 仓库
// 用两种贪心策略重构斜堆的字典序最小/最大插入序列

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
struct Node { int L=0, R=0, P=0; };
vector<Node> initial_tree;

vector<int> find_candidates(const vector<Node>& tree, int root) {
    if (root == 0) return {};
    int vk = 0;
    int curr = root;
    while(curr != 0) {
        if (tree[curr].R == 0) { vk = curr; break; }
        curr = tree[curr].L;
    }
    if (vk == 0) return {};
    vector<int> candidates = {vk};
    int vk1 = tree[vk].L;
    if (vk1 && tree[vk1].L == 0 && tree[vk1].R == 0)
        candidates.push_back(vk1);
    return candidates;
}

int reverse_insertion(vector<Node>& tree, int x, int root) {
    int w = tree[x].L, px = tree[x].P;
    if (px == 0) { root = w; if (w) tree[w].P = 0; }
    else { tree[px].L = w; if (w) tree[w].P = px; }
    tree[x].L = tree[x].R = tree[x].P = 0;
    int curr = px;
    while (curr != 0) {
        swap(tree[curr].L, tree[curr].R);
        curr = tree[curr].P;
    }
    return root;
}

vector<int> find_permutation(int strategy) {
    vector<Node> tree = initial_tree;
    int root = (N > 0) ? 1 : 0;
    vector<int> reversed_P;
    for (int i = 0; i < N; ++i) {
        auto candidates = find_candidates(tree, root);
        if (candidates.empty()) return {};
        int x = (strategy == 0)
            ? *max_element(candidates.begin(), candidates.end())
            : *min_element(candidates.begin(), candidates.end());
        reversed_P.push_back(x);
        root = reverse_insertion(tree, x, root);
    }
    reverse(reversed_P.begin(), reversed_P.end());
    return reversed_P;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    if (!(cin >> N)) return 0;
    initial_tree.resize(N + 1);
    for (int i = 1; i <= N; ++i) {
        int l, r;
        cin >> l >> r;
        initial_tree[i].L = l;
        initial_tree[i].R = r;
        if (l) initial_tree[l].P = i;
        if (r) initial_tree[r].P = i;
    }
    auto min_P = find_permutation(0);
    if (min_P.empty()) { cout << "impossible\n"; return 0; }
    auto max_P = find_permutation(1);
    for (int i = 0; i < N; ++i) cout << min_P[i] << (i==N-1?"":" ");
    cout << "\n";
    for (int i = 0; i < N; ++i) cout << max_P[i] << (i==N-1?"":" ");
    cout << "\n";
    return 0;
}
