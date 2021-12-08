#!/usr/bin/env python3

import sys

L = [x.strip() for x in sys.stdin.readlines()]
n = len(L[0])
cnt = n * [0]
for w in L:
    for i in range(n):
        if w[i] == '0':
            cnt[i] -= 1
        else:
            cnt[i] += 1
num_a = 0
num_b = 0
for i in range(n):
    num_a *= 2
    num_b *= 2
    if cnt[i] > 0:
        num_a += 1
    else:
        num_b += 1
sys.stdout.write(f'{num_a*num_b}\n')


def filter(start, ns, kind):
    #print(start, kind, ns)
    if len(ns) == 1:
        return ns[0]
    cnt = 0
    for w in ns:
        if w[start] == '1':
            cnt += 1
        else:
            cnt -= 1
    ps = []
    keep = '1' if (cnt>=0) ^ kind else '0'
    for w in ns:
        if w[start] == keep:
            ps.append(w)
    return filter(start + 1, ps, kind)

a = int(filter(0, L, True), 2)
b = int(filter(0, L, False), 2)
sys.stdout.write(f'{a} {b} {a*b}\n')