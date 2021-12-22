#!/usr/bin/env python3

from collections import defaultdict
import sys

now = None
nxt = defaultdict(int)
nxt[((4 - 1, 3 - 1), (0, 0))] = 1

done = defaultdict(int)

turn = 0
while nxt:
    i = turn % 2
    now = nxt
    nxt = defaultdict(int)
    for (p, s), cnt in now.items():
        if s[0] >= 21 or s[1] >= 21:
            done[(p, s)] += cnt
            continue
        for d1 in range(1, 4):
            for d2 in range(1, 4):
                for d3 in range(1, 4):
                    pp = list(p)
                    ss = list(s)
                    pp[i] += d1 + d2 + d3
                    pp[i] %= 10
                    ss[i] += 1 + pp[i]
                    nxt[(tuple(pp), tuple(ss))] += cnt
    turn += 1
    #print(f'len {len(nxt)} {sorted(nxt.items())}')

w = [0, 0]
for (p, s), cnt in done.items():
    for i in range(2):
        if s[i] >= 21:
            w[i] += cnt
sys.stdout.write(f'{w}\n')