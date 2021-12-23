#!/usr/bin/env python3

# NOTE: This is too slow. See p22b.py for something fast enough.

from collections import defaultdict
import re
import sys

instructions = [
    re.sub('[^0-9onf-]', ' ', x).strip().split()
    for x in sys.stdin.readlines()
]
instructions = [(x[0], tuple(int(x[i + 1]) for i in range(6)))
                for x in instructions]

#print(instructions)

vs = [set() for _ in range(3)]
for _, (x0, x1, y0, y1, z0, z1) in instructions:
    if True or all(-50 <= c <= 50 for c in [x0, x1, y0, y1, z0, z1]):
        vs[0].add(x0)
        vs[0].add(x1 + 1)
        vs[1].add(y0)
        vs[1].add(y1 + 1)
        vs[2].add(z0)
        vs[2].add(z1 + 1)
for i in range(3):
    vs[i] = sorted(vs[i])
    print(f'i={i} min={min(vs[i])} max={max(vs[i])} len={len(vs[i])}')

#print(vs)

mentions = [defaultdict(list) for _ in range(3)]
for x in vs[0]:
    for i in range(len(instructions))[::-1]:
        x0 = instructions[i][1][0]
        x1 = instructions[i][1][1]
        if x0 <= x <= x1:
            mentions[0][x].append(i)
for y in vs[1]:
    for i in range(len(instructions))[::-1]:
        y0 = instructions[i][1][2]
        y1 = instructions[i][1][3]
        if y0 <= y <= y1:
            mentions[1][y].append(i)
for z in vs[2]:
    for i in range(len(instructions))[::-1]:
        z0 = instructions[i][1][4]
        z1 = instructions[i][1][5]
        if z0 <= z <= z1:
            mentions[2][z].append(i)

ans = 0
for i in range(len(vs[0]) - 1):
    print(f'i={i}')
    for j in range(len(vs[1]) - 1):
        for k in range(len(vs[2]) - 1):
            on = False
            ms = [
                mentions[0][vs[0][i]], mentions[1][vs[1][j]],
                mentions[2][vs[2][k]]
            ]
            ps = [0, 0, 0]
            #print(ms)
            while all(ps[d] < len(ms[d]) for d in range(3)):
                last = min(ms[d][ps[d]] for d in range(3))
                if all(last == ms[d][ps[d]] for d in range(3)):
                    #print(
                    #    f'({vs[0][i]},{vs[1][j]},{vs[2][k]}) appears in {instructions[last]}'
                    #)
                    on = instructions[last][0] == 'on'
                    break
                for d in range(3):
                    while ps[d] < len(ms[d]) and ms[d][ps[d]] > last:
                        ps[d] += 1
            if on:
                ans += (vs[0][i + 1] - vs[0][i]) * (
                    vs[1][j + 1] - vs[1][j]) * (vs[2][k + 1] - vs[2][k])
sys.stdout.write(f'ans {ans}\n')
