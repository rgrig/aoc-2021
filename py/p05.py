#!/usr/bin/env

from collections import defaultdict
import sys

segs = [x.split('->') for x in sys.stdin.readlines()]
segs = [[y.strip().split(',') for y in x] for x in segs]
segs = [[[int(x1), int(y1)], [int(x2), int(y2)]] for [[x1,y1], [x2,y2]] in segs]


overlaps = set()
covered = defaultdict(int)
for [[x1,y1], [x2,y2]] in segs:
    #print(f'({x1},{y1})->({x2},{y2})')
    dx = dy = 0
    if x2 > x1:
        dx = 1
    elif x2 < x1:
        dx = -1
    if y2 > y1:
        dy = 1
    elif y2 < y1:
        dy = -1
    #if dx * dy != 0:
    #    continue
    x, y = x1, y1
    while True:
        #print(f' ({x},{y})')
        covered[(x,y)] += 1
        if covered[(x,y)] > 1:
            overlaps.add((x,y))
        if x == x2 and y == y2:
            break
        x += dx
        y += dy
sys.stdout.write(f'{len(overlaps)}\n')
