#!/usr/bin/env python3

from collections import defaultdict
import sys

defaultenc = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

enc = defaultdict(list)
s = list('abcdefg')
while True:
    digits = set()
    for ss in defaultenc:
        d = set()
        for c in ss:
            d.add(s[ord(c)-ord('a')])
        digits.add(tuple(sorted(d)))
    enc[tuple(sorted(digits))] = list(s)
    i = len(s) - 2
    m = s[i+1]
    while i >= 0:
        if s[i] < m:
            jj = i + 1
            j = i + 2
            while j < len(s):
                if s[jj] > s[j] and s[j] > s[i]:
                    jj = j
                j += 1
            s = s[:i] + [s[jj]] + sorted(s[i:jj]+s[jj+1:])
            break
        else:
            m = s[i]
        i -= 1
    if i < 0:
        break

#print(enc)

def solve(digits, display):
    digits = tuple(sorted(tuple(sorted(d)) for d in digits))
    perm = enc[digits]
    num = 0
    for d in display:
        v = set()
        for s in d:
            v.add(chr(perm.index(s) + ord('a')))
        v = ''.join(sorted(v))
        num = 10 * num + defaultenc.index(v)
    #print(num)
    return num

ans = 0
ans2 = 0
for line in sys.stdin:
    ws = line.split()
    ans2 += solve(ws[:10], ws[11:])
    ws = ws[11:]
    for w in ws:
        if len(w) in [2,4,3,7]:
            #print(w)
            ans += 1
sys.stdout.write(f'{ans}\n')
sys.stdout.write(f'ans2 {ans2}\n')