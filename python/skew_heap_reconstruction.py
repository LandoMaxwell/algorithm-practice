#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
斜堆插入序列重构算法
算法思路: 逆向模拟插入过程，每次找候选节点并还原堆结构
"""

from typing import List, Tuple


class SkewHeapReconstruction:
    def __init__(self):
        self.N = 0
        self.tree = []

    def solve(self):
        import sys
        input_data = sys.stdin.read().split()
        idx = 0
        self.N = int(input_data[idx]); idx += 1
        self.tree = [{'L': 0, 'R': 0, 'P': 0} for _ in range(self.N + 1)]
        for i in range(1, self.N + 1):
            l, r = int(input_data[idx]), int(input_data[idx+1]); idx += 2
            self.tree[i]['L'] = l
            self.tree[i]['R'] = r
            if l: self.tree[l]['P'] = i
            if r: self.tree[r]['P'] = i
        min_p = self._find_permutation(0)
        max_p = self._find_permutation(1)
        if not min_p:
            print('impossible')
            return
        print(' '.join(map(str, min_p)))
        print(' '.join(map(str, max_p)))

    def _find_candidates(self, tree, root):
        if root == 0: return []
        vk = 0
        curr = root
        while curr:
            if tree[curr]['R'] == 0:
                vk = curr; break
            curr = tree[curr]['L']
        if vk == 0: return []
        candidates = [vk]
        vk1 = tree[vk]['L']
        if vk1 and tree[vk1]['L'] == 0 and tree[vk1]['R'] == 0:
            candidates.append(vk1)
        return candidates

    def _reverse_insertion(self, tree, x, root):
        w = tree[x]['L']
        px = tree[x]['P']
        if px == 0:
            root = w
            if w: tree[w]['P'] = 0
        else:
            tree[px]['L'] = w
            if w: tree[w]['P'] = px
        tree[x] = {'L': 0, 'R': 0, 'P': 0}
        curr = px
        while curr:
            tree[curr]['L'], tree[curr]['R'] = tree[curr]['R'], tree[curr]['L']
            curr = tree[curr]['P']
        return root

    def _find_permutation(self, strategy):
        import copy
        tree = copy.deepcopy(self.tree)
        root = 1 if self.N > 0 else 0
        result = []
        for _ in range(self.N):
            candidates = self._find_candidates(tree, root)
            if not candidates: return []
            x = max(candidates) if strategy == 0 else min(candidates)
            result.append(x)
            root = self._reverse_insertion(tree, x, root)
        result.reverse()
        return result
