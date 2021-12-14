#!/usr/bin/env python3

import sys

points = []
folds = []

for line in sys.stdin:
    line = line.strip()
    if line.startswith('fold along x'):
        folds.append((0, int(line[len('fold along x='):])))
    elif line.startswith('fold along y'):
        folds.append((1, int(line[len('fold along y='):])))
    elif line:
        line = line.split(',')
        points.append([int(line[0]), int(line[1])])

for d, dp in folds:
    for p in points:
        if p[d] > dp:
            p[d] = 2 * dp - p[d]
points = set(tuple(p) for p in points)
MY = max(p[1] for p in points)
MX = max(p[0] for p in points)
for y in range(MY + 1):
    for x in range(MX + 1):
        c = '#' if (x, y) in points else ' '
        sys.stdout.write(c)
    sys.stdout.write('\n')

sys.stdout.write(f'{len(points)}\n')
#(points)