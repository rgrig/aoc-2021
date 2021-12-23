#!/usr/bin/env python3

from bisect import bisect, bisect_left
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
    for i in range(len(instructions)):
        x0 = instructions[i][1][0]
        x1 = instructions[i][1][1]
        if x0 <= x <= x1:
            mentions[0][x].append(i)
for y in vs[1]:
    for i in range(len(instructions)):
        y0 = instructions[i][1][2]
        y1 = instructions[i][1][3]
        if y0 <= y <= y1:
            mentions[1][y].append(i)

ops = 0
ans = 0
for i in range(len(vs[0]) - 1):
    #print(f'i={i}')
    dx = vs[0][i + 1] - vs[0][i]
    for j in range(len(vs[1]) - 1):
        ms = sorted(set(mentions[0][vs[0][i]]) & set(mentions[1][vs[1][j]]))
        S = dx * (vs[1][j + 1] - vs[1][j])
        zon = []  # TODO: use a tree
        for m in ms:
            ops += 1
            cmd, (x0, x1, y0, y1, z0, z1) = instructions[m]
            assert x0 <= vs[0][i] <= x1
            assert y0 <= vs[1][j] <= y1
            z1 += 1
            #print(f'before {zon}')
            k0 = bisect(zon, z0)
            k1 = bisect(zon, z1)
            #print(f'k0 {k0} k1 {k1}')
            if cmd == 'on':
                #print(f'add [{z0},{z1})')
                if k0 % 2 == 1:
                    k0 -= 1
                    z0 = zon[k0]
                if k1 % 2 == 1:
                    z1 = zon[k1]
                    k1 += 1
                zon = zon[:k0] + [z0, z1] + zon[k1:]
            else:
                #print(f'del [{z0},{z1})')
                nzon = zon[:k0 & ~1]
                if k0 & 1:
                    nzon.extend([zon[k0 - 1], z0])
                if k1 & 1:
                    nzon.extend([z1, zon[k1]])
                    k1 += 1
                nzon.extend(zon[k1:])
                zon = nzon
            #print(f'after  {zon}')
            #assert len(set(zon)) == len(zon)
            #assert len(zon) % 2 == 0
        for k in range(0, len(zon), 2):
            ans += S * (zon[k + 1] - zon[k])

sys.stdout.write(f'ans {ans}\n')
print(f'ops {ops}')