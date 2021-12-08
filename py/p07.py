#!/usr/bin/env python3

from collections import defaultdict
import math
import sys

pos = [int(x) for x in sys.stdin.read().strip().split(',')]
pos.sort()
align = pos[len(pos)//2]
print(align)
ans = sum([abs(x-align) for x in pos])

sys.stdout.write(f'{ans}\n')

ans = None
for align in range(pos[0],pos[-1]+1):
    cost = sum([abs(x-align)*(abs(x-align)+1)//2 for x in pos])
    if ans is None or ans > cost:
        ans = cost
sys.stdout.write(f'{ans}\n')
