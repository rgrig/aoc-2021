#!/usr/bin/env python3

import math
import re
import sys


def solve(line):
    line = re.sub('[^0-9-]', ' ', line)
    [xmin, xmax, ymin, ymax] = [int(a) for a in line.split()]
    ok = set()
    vx = 1
    while vx <= xmax:
        if True:
            for t in range(0, vx + 1):
                x = vx * t - t * (t - 1) // 2
                if not (xmin <= x and x <= xmax):
                    continue
                for y in range(ymin, ymax + 1):
                    a = y + t * (t - 1) // 2
                    if a % t == 0:
                        vy = a // t
                        ok.add((vx, vy))
        x = vx * (vx + 1) // 2
        if xmin <= x and x <= xmax:
            for y in range(ymin, ymax + 1):
                for t in range(vx + 1, 2 * abs(y) + 1):
                    if 2 * y % t == 0:
                        if (2 * y // t + t - 1) % 2 == 0:
                            vy = (2 * y // t + t - 1) // 2
                            ok.add((vx, vy))
        vx += 1
    sys.stdout.write(f'{len(ok)}\n')


for line in sys.stdin:
    solve(line)