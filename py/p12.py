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


def go(y, S):
    print(y, S)
    if y == 'start':
        return 1
    if (y, frozenset(S)) in C:
        return C[(y, frozenset(S))]
    r = 0
    SS = set(S)
    if y[0] in ascii_lowercase:
        SS.add(y)
    for x in G[y]:
        if x not in SS:
            r += go(x, SS)
    C[(y, frozenset(S))] = r
    return r


ans = go('end', set())
sys.stdout.write(f'{ans}\n')