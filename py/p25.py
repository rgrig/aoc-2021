#!/usr/bin/env python3

import re
import sys

M = [list(x.strip()) for x in sys.stdin.readlines()]

m = len(M)
n = len(M[0])

t = 0
progress = True
while progress:
    progress = False
    N = list(list(row) for row in M)
    for i in range(m):
        for j in range(n):
            if N[i][j] != '>':
                continue
            if N[i][(j + 1) % n] == '.':
                assert M[i][(j + 1) % n] == '.'
                progress = True
                M[i][j] = '.'
                M[i][(j + 1) % n] = '>'
    N = list(list(row) for row in M)
    for i in range(m):
        for j in range(n):
            if N[i][j] != 'v':
                continue
            if N[(i + 1) % m][j] == '.':
                assert M[(i + 1) % m][j] == '.'
                progress = True
                M[i][j] = '.'
                M[(i + 1) % m][j] = 'v'
    t += 1
    if False:
        print(f'time {t}')
        for row in M:
            print(''.join(row))
        print()
    if t % 1000 == 0:
        print(f'prog {t}')
sys.stdout.write(f'answer {t}\n')
