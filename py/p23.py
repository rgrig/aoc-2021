#!/usr/bin/env python3

from bisect import bisect, bisect_left
from collections import defaultdict, deque
from heapq import heappop, heappush
import math
import re
import sys

input = sys.stdin.readlines()

cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

dist = {}
todo = []


def F(x):
    return tuple(tuple(x for x in row) for row in x)


destination = F([
    '#############\n', '#...........#\n', '###A#B#C#D###\n', '  #A#B#C#D#\n',
    '  #A#B#C#D#\n', '  #A#B#C#D#\n', '  #########\n'
])

dist[F(input)] = 0
heappush(todo, (0, input))

ops = 0

while todo:
    d, x = heappop(todo)
    ops += 1
    if ops % 100 == 0:
        print(f'ops {ops} dist {d}')
    if False:
        sys.stdout.write(f'processing cost {d}:\n')
        for row in x:
            sys.stdout.write('  {}'.format(''.join(row)))
    if F(x) == destination:
        sys.stdout.write(f'ans {d}\n')
        break
    # move out
    for j in [3, 5, 7, 9]:
        i = 1
        while x[i][j] == '.':
            i += 1
        if x[i][j] != '#':
            #print(f'move {x[i][j]} out of col {j}')
            # go left
            jj = j
            while x[1][jj] == '.':
                if jj not in [3, 5, 7, 9]:
                    y = [list(row) for row in x]
                    y[1][jj] = y[i][j]
                    y[i][j] = '.'
                    step = (abs(i - 1) + abs(j - jj)) * cost[x[i][j]]
                    #print(f'moving to col {jj}, step {step} result {y}')
                    fy = F(y)
                    #print(fy)
                    if fy not in dist or dist[fy] > d + step:
                        dist[fy] = d + step
                        heappush(todo, (d + step, y))
                jj -= 1
            # go right
            jj = j
            while x[1][jj] == '.':
                if jj not in [3, 5, 7, 9]:
                    y = [list(row) for row in x]
                    y[1][jj] = y[i][j]
                    y[i][j] = '.'
                    step = (abs(i - 1) + abs(j - jj)) * cost[x[i][j]]
                    fy = F(y)
                    if fy not in dist or dist[fy] > d + step:
                        dist[fy] = d + step
                        heappush(todo, (d + step, y))
                jj += 1
    i = None
    # move in
    for j in range(1, 12):
        if x[1][j] != '.':
            jj = 3 + 2 * (ord(x[1][j]) - ord('A'))
            if jj < j and any(x[1][jjj] != '.' for jjj in range(jj, j)):
                continue
            if jj > j and any(x[1][jjj] != '.'
                              for jjj in range(j + 1, jj + 1)):
                continue
            if any((x[ii][jj] not in ['.', x[1][j]]) for ii in range(2, 6)):
                continue
            ii = 2
            if True:
                while x[ii + 1][jj] not in ['#', x[1][j]]:
                    ii += 1
            while x[ii][jj] == '.':
                #print(f'move {x[1][j]} into its home')
                y = [list(row) for row in x]
                y[ii][jj] = x[1][j]
                y[1][j] = '.'
                step = ((ii - 1) + abs(j - jj)) * cost[x[1][j]]
                fy = F(y)
                if fy not in dist or dist[fy] > d + step:
                    dist[fy] = d + step
                    heappush(todo, (d + step, y))
                ii += 1

#print(dist)
#sys.stdout.write(f'ans {dist[destination]}')
