#!/usr/bin/env python3

import sys

lines = [int(x) for x in sys.stdin.readlines()]
ans = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        ans += 1
sys.stdout.write(f'{ans}\n')

ans2 = 0
n = 3
for i in range(n+1, len(lines)+1):
    if sum(lines[i-n:i]) > sum(lines[i-1-n:i-1]):
        ans2 += 1
sys.stdout.write(f'{ans2}\n')