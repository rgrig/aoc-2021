#!/usr/bin/env python3

from collections import deque
import sys

M = [x.strip() for x in sys.stdin.readlines()]
M = [[int(x) for x in y] for y in M]

im = len(M)
jm = len(M[0])

ans = 0
ans2 = None
for t in range(1000):
    seen = [[0 for _ in range(jm)] for _ in range(im)]
    q = deque()
    for i in range(im):
        for j in range(jm):
            M[i][j] += 1
            if M[i][j] > 9:
                seen[i][j] = True
                q.append((i, j))
    while q:
        i, j = q.popleft()
        for ii in [i - 1, i, i + 1]:
            for jj in [j - 1, j, j + 1]:
                if not (0 <= ii and ii < im):
                    continue
                if not (0 <= jj and jj < jm):
                    continue
                if seen[ii][jj]:
                    continue
                M[ii][jj] += 1
                if M[ii][jj] > 9:
                    seen[ii][jj] = True
                    q.append((ii, jj))
    fn = 0
    for i in range(im):
        for j in range(jm):
            if M[i][j] > 9:
                fn += 1
                M[i][j] = 0
    if t < 100:
        ans += fn
    if ans2 is None and fn == 100:
        ans2 = t + 1
sys.stdout.write(f'{ans}\n{ans2}\n')