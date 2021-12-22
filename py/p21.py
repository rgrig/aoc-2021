#!/usr/bin/env python3

import sys

p = [4 - 1, 3 - 1]
s = [0, 0]

turn = 0
last = 0
while s[0] < 1000 and s[1] < 1000:
    i = turn % 2
    die = 0
    for _ in range(3):
        last += 1
        die += last
    p[i] += die
    p[i] %= 10
    s[i] += 1 + p[i]
    turn += 1

sys.stdout.write(
    f'last={last} loser={min(s)} winner={max(s)} ans={last*min(s)}\n')
