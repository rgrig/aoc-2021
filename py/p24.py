#!/usr/bin/env python3

from bisect import bisect, bisect_left
from collections import defaultdict, deque
from heapq import heappop, heappush
import math
import re
import sys

A = [10, 14, 14, -13, 10, -13, -7, 11, 10, 13, -4, -9, -13, -9]
B = [2, 13, 13, 9, 15, 3, 6, 5, 16, 1, 6, 3, 7, 9]
C = [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]


def go(I, ii, jj):
    z = 0
    for i in range(ii, jj):
        w = ord(I[i - ii]) - ord('0')
        print(
            f'i {i} has A={A[i]} B={B[i]} C={C[i]} w={w} z={z} d={z % 26 + A[i]}'
        )
        if w == z % 26 + A[i]:
            if C[i]:
                z = z // 26
        else:
            if C[i] == 0:
                z = z * 26
            z += w + B[i]
    return z


def f(i, z, w):
    if w == z % 26 + A[i]:
        if C[i]:
            z = z // 26
    else:
        if C[i] == 0:
            z = z * 26
        z += w + B[i]
    return z


zs = [defaultdict(list) for _ in range(15)]
zs[0][0] = []
for i in range(14):
    for z in zs[i]:
        for w in range(10):
            zz = f(i, z, w)
            if zz <= 26**sum(C[i:]):
                zs[i + 1][zz].append((z, w))
    print(len(zs[i + 1]))
gz = [set() for _ in range(15)]
gz[14].add(0)
for i in range(14, 0, -1):
    for z, pred in zs[i].items():
        if z not in gz[i]:
            continue
        for zz, ww in pred:
            if ww != 0:
                gz[i - 1].add(zz)
sol = 0
z = 0
for i in range(14):
    for w in range(1, 10):
        zz = f(i, z, w)
        if zz in gz[i + 1]:
            sol = 10 * sol + w
            z = zz
            break
    print(f'w={w}')
print(f'{sol:014}')

if True:
    for I in sys.stdin:
        print(go(I, 0, 14))

if False:
    for x in range(9999999, -1, -1):
        I = f'{x:07}'
        if go(I, 7, 14) == 0:
            print(x)
            break
    for x in range(9999999, -1, -1):
        I = f'{x:07}'
        if go(I, 0, 7) == 0:
            print(x)
            break
