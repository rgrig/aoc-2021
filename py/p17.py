#!/usr/bin/env python3

import math
import re
import sys


def solve(line):
    line = re.sub('[^0-9-]', ' ', line)
    [xmin, xmax, ymin, ymax] = [int(a) for a in line.split()]

    # O(Δy⋅max{|ymin|,|ymax|})
    assert xmin > 0
    vymax = None
    for y in range(ymin, ymax + 1):
        for t in range(1, 2 * abs(y) + 1):
            ok = False
            vx = math.ceil(-0.5 + math.sqrt(2 * xmin + 1 / 4))
            if vx <= t:
                ok = True
                #print(f'vx={vx} t={t} (maxed)')
            vx = math.floor((t - 1) / 2 + xmax / t)
            if False:
                # Large vy corresponds to small vx (aka 'maxed'). But I'm not sure
                # if the discrete nature of the problem messes this up. If so, enable
                # the following check
                if vx > max(t, (t - 1) / 2 + xmin / t):
                    ok = True
                    print(f'vx={vx} t={t} (still going)')
            if not ok:
                continue
            if 2 * y % t == 0:
                vy2 = 2 * y // t + t - 1
                if vy2 % 2 == 0:
                    vy = vy2 // 2
                    if vymax is None or vymax < vy:
                        vymax = vy
                        print(f'vymax={vymax}')
    sys.stdout.write(f'{vymax}\n')

    # first/original solution follows follows; slightly slower than the one above
    bvmax = None
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymin + 1):
            v0 = int(math.sqrt(2 * abs(x)))
            for t in range(max(1, v0 - 10), v0 + 10):
                for tt in range(t, abs(2 * y) + 1):
                    if 2 * y % tt == 0:
                        if (2 * y // tt - 1 + tt) % 2 == 0:
                            vmax = (2 * y // tt - 1 + tt) // 2
                            if bvmax is None or vmax > bvmax:
                                bvmax = vmax
    ymax = bvmax * bvmax - bvmax * (bvmax - 1) // 2
    sys.stdout.write(f'{bvmax} {ymax}\n')


for line in sys.stdin:
    solve(line)