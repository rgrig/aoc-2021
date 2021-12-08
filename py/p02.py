#!/usr/bin/env python3

import sys

lines = [x.split() for x in sys.stdin.readlines()]
lines = [(w[0], int(w[1])) for w in lines]

dx = dy = 0
for cmd, d in lines:
    if cmd == 'forward':
        dx += d
    elif cmd == 'down':
        dy += d
    else:
        dy -= d
sys.stdout.write(f'{dx*dy}\n')

aim = 0
x = y = 0
for cmd, d in lines:
    if cmd == 'forward':
        x += d
        y += aim*d
    elif cmd == 'down':
        aim += d
    else:
        aim -= d
sys.stdout.write(f'{x*y}\n')
