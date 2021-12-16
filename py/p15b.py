#!/usr/bin/env python3

import heapq
import sys

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

M = [x.strip() for x in sys.stdin.readlines()]
M = [[int(c) for c in row] for row in M]

ii = len(M)
jj = len(M[0])

MM = [[0 for _ in range(5 * ii)] for _ in range(5 * jj)]
for i in range(ii):
    for j in range(jj):
        MM[i][j] = M[i][j]
for a in range(5):
    for b in range(5):
        if a > 0:
            for i in range(ii):
                for j in range(jj):
                    MM[ii * a + i][jj * b +
                                   j] = (MM[ii *
                                            (a - 1) + i][jj * b + j] % 9) + 1
        if b > 0:
            for i in range(ii):
                for j in range(jj):
                    MM[ii * a + i][jj * b +
                                   j] = (MM[ii * a + i][jj *
                                                        (b - 1) + j] % 9) + 1
M = MM
ii *= 5
jj *= 5
print(ii, jj)
#print(MM)

D = [[None for _ in range(jj)] for _ in range(ii)]
S = [[False for _ in range(jj)] for _ in range(ii)]
Q = []

D[0][0] = 0
heapq.heappush(Q, (D[0][0], (0, 0)))

while Q:
    d, (i, j) = heapq.heappop(Q)
    #print(d, i, j)
    if S[i][j]:
        continue
    assert D[i][j] == d
    S[i][j] = True
    if i == ii - 1 and j == jj + 1:
        break
    for dir in range(4):
        i2 = i + DX[dir]
        j2 = j + DY[dir]
        if not (0 <= i2 and i2 < ii):
            continue
        if not (0 <= j2 and j2 < jj):
            continue
        d2 = d + M[i2][j2]
        if D[i2][j2] is None or d2 < D[i2][j2]:
            D[i2][j2] = d2
            heapq.heappush(Q, (D[i2][j2], (i2, j2)))

sys.stdout.write(f'{D[ii-1][jj-1]}\n')
