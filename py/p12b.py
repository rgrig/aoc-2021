#!/usr/bin/env python3

from collections import defaultdict
from string import ascii_lowercase
import sys

input = [x.strip() for x in sys.stdin.readlines()]
edges = [x.split('-') for x in input]

G = defaultdict(list)
for [a, b] in edges:
    G[a].append(b)
    G[b].append(a)

C = {}


def go(y, S, s):
    print(y, S, s)
    if y == 'start':
        return 1
    if (y, frozenset(S), s) in C:
        return C[(y, frozenset(S), s)]
    r = 0
    SS = list(S)
    if y[0] in ascii_lowercase:
        SS.append(y)
        if y in S:
            assert s is None and y not in ['start', 'end']
            s = y
    for x in G[y]:
        if x not in SS or (s is None and x not in ['start', 'end']):
            r += go(x, SS, s)
    C[(y, frozenset(S), s)] = r
    return r


ans = go('end', [], None)
sys.stdout.write(f'{ans}\n')
