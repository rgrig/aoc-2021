#!/usr/bin/env python3

from collections import deque
import sys

score = {')': 3, ']': 57, '}': 1197, '>': 25137}
pair = {'(': ')', '[': ']', '{': '}', '<': '>'}


def match(a, b):
    return pair[a] == b


acscores = []

ans = 0
for line in sys.stdin:
    line = line.strip()
    s = deque()
    for c in line:
        bad = False
        if c in '([{<':
            s.append(c)
        elif c in ')]}>':
            if len(s) == 0:
                bad = True
            else:
                cc = s.pop()
                if not match(cc, c):
                    #print(' ', ans)
                    ans += score[c]
                    bad = True
            if bad:
                #print(f'{cc}{c} {line}')
                break
    if not bad:
        ac = 0
        while s:
            ac = 5 * ac + '([{<'.index(s.pop()) + 1
        acscores.append(ac)
sys.stdout.write(f'{ans}\n')
acscores.sort()
#print(acscores)
ans2 = acscores[len(acscores) // 2]
sys.stdout.write(f'{ans2}\n')
