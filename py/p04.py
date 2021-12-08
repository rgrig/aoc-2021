#!/usr/bin/env python3

from collections import defaultdict
import sys

all_input = [x.strip() for x in sys.stdin.readlines()]

moves, all_input = all_input[0], all_input[1:]
moves = [int(x) for x in moves.split(',')]
print(moves)
boards = []
for i in range(0,len(all_input)-5,6):
    B = []
    for j in range(5):
        B.append([int(x) for x in all_input[i+j+1].split()])
    boards.append(B)

pos = defaultdict(list)
for i in range(len(boards)):
    for j in range(len(boards[i])):
        for k in range(len(boards[i][j])):
            pos[boards[i][j][k]].append((i,j,k))

cols = [[0 for _ in range(5)] for _ in range(len(boards))]
rows = [[0 for _ in range(5)] for _ in range(len(boards))]
already_won = set()
for m in moves:
    for b, i, j in pos[m]:
        if b in already_won:
            continue
        rows[b][i] += 1
        cols[b][j] += 1
        boards[b][i][j] = -1
        if rows[b][i] == 5 or cols[b][j] == 5:
            s = 0
            for r in boards[b]:
                for x in r:
                    if x > 0:
                        s += x
            ans = s * m
            already_won.add(b)
            sys.stdout.write(f'sum {s} move {m} ans {s*m}\n')
