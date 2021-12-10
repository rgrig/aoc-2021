#!/usr/bin/env python3

from collections import deque
import sys

DI = [1, 0, -1, 0]
DJ = [0, 1, 0, -1]

basins = []

map = [x.strip() for x in sys.stdin.readlines()]
m = len(map)
n = len(map[0])
nmap = [[10 for j in range(n + 2)] for i in range(m + 2)]
seen = [[False for j in range(n + 2)] for i in range(m + 2)]

for i in range(m):
    for j in range(n):
        nmap[i + 1][j + 1] = ord(map[i][j]) - ord('0')
#print(map)
#print(nmap)
ans = 0
for i in range(m):
    for j in range(n):
        ok = True
        for d in range(4):
            ok = ok and (nmap[i + 1 + DI[d]][j + 1 + DJ[d]] >
                         nmap[i + 1][j + 1])
        if ok:
            #print(i, j, nmap[i + 1][j + 1])
            ans += nmap[i + 1][j + 1] + 1
            queue = deque()
            queue.append((i, j))
            seen[i + 1][j + 1] = True
            sz = 1
            while queue:
                (ii, jj) = queue.popleft()
                for dd in range(4):
                    iii = ii + DI[dd]
                    jjj = jj + DJ[dd]
                    if not seen[iii + 1][
                            jjj + 1] and nmap[iii + 1][jjj + 1] > nmap[ii + 1][
                                jj + 1] and nmap[iii + 1][jjj + 1] < 9:
                        seen[iii + 1][jjj + 1] = True
                        queue.append((iii, jjj))
                        sz += 1
            basins.append(sz)
sys.stdout.write(f'{ans}\n')

basins.sort()
sys.stdout.write(f'{basins[-1]*basins[-2]*basins[-3]}\n')
#print(basins)
