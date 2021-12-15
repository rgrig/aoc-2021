#!/usr/bin/env python3

from collections import defaultdict
import sys

pattern = sys.stdin.readline().strip()
rules = {}
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    line = line.split(' -> ')
    src = line[0]
    tgt = line[1]
    assert src not in rules
    rules[src] = tgt

#print(pattern)
now = defaultdict(int)
for i in range(2, len(pattern) + 1):
    now[pattern[i - 2:i]] += 1

#print(sorted(now.items()))
for _ in range(40):
    nxt = defaultdict(int)
    for p, c in now.items():
        if p in rules:
            m = rules[p]
            nxt[p[0] + m] += c
            nxt[m + p[1]] += c
        else:
            nxt[p] += 1
    now = nxt
    #print(sorted(now.items()))

cnt = defaultdict(int)
for p, c in now.items():
    cnt[p[0]] += c
    cnt[p[1]] += c
cnt[pattern[0]] += 1
cnt[pattern[-1]] += 1
cnt = sorted((c // 2, l) for (l, c) in cnt.items())

#print(cnt)
#print(sum(c for c, _ in cnt))

ans = (cnt[-1][0] - cnt[0][0])

sys.stdout.write(f'{ans}\n')

# NBBBCNCCNBBNBNBBCHBHHBCHB
#
