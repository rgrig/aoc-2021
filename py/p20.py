#!/usr/bin/env python3

import sys

algo = sys.stdin.readline().strip()
sys.stdin.readline()
image = [x.strip() for x in sys.stdin.readlines()]

inf = False
m = len(image)
n = len(image[0])
I = set()
for i in range(m):
    for j in range(n):
        if image[i][j] == '#':
            I.add((i, j))


def V(i, j):
    global inf, I
    return inf ^ ((i, j) in I)


for _ in range(50):
    #print(f'inf={inf} I={sorted(I)}')
    if inf:
        ninf = algo[-1] == '#'
    else:
        ninf = algo[0] == '#'
    nI = set()
    mi = min(i for i, _ in I)
    Mi = max(i for i, _ in I)
    mj = min(j for _, j in I)
    Mj = max(j for _, j in I)
    for i in range(mi - 1, Mi + 2):
        for j in range(mj - 1, Mj + 2):
            index = 0
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    index = 2 * index + V(ii, jj)
            p = algo[index] == '#'
            if p != ninf:
                nI.add((i, j))
    I = nI
    inf = ninf

assert not inf
sys.stdout.write(f'ans {len(I)}\n')
