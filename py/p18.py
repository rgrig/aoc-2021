#!/usr/bin/env python3

from string import digits
import sys


def add(X, Y):
    Z = ['['] + X + Y + [']']
    #print('X', X)
    #print('Y', Y)
    progress = True
    while progress:
        #print('Z', Z)
        progress = False
        nest = 0
        i = 0
        while i < len(Z):
            #print('i', i, 'nest', nest)
            if Z[i] == '[':
                nest += 1
            elif Z[i] == ']':
                nest -= 1
            else:
                assert type(Z[i]) == int
                j = i + 1
                while j < len(Z) and type(Z[j]) == int:
                    j += 1
                if nest >= 5 and j < len(Z) and Z[j] == ']' and j - i == 2:
                    progress = True
                    j = i - 1
                    while j >= 0:
                        if type(Z[j]) == int:
                            Z[j] += Z[i]
                            break
                        j -= 1
                    j = i + 2
                    while j < len(Z):
                        if type(Z[j]) == int:
                            Z[j] += Z[i + 1]
                            break
                        j += 1
                    Z[i - 1:i + 3] = [0]
                    break
                else:
                    i = j - 1
            i += 1
        #print('Z', Z)
        assert i < len(Z) or nest == 0
        if progress:
            continue
        i = 0
        while i < len(Z):
            if type(Z[i]) == int and Z[i] > 9:
                progress = True
                a = Z[i] // 2
                b = Z[i] - a
                Z[i:i + 1] = ['[', a, b, ']']
                break
            i += 1
    #print('Z', Z)
    return Z


def magnitude(X, a, c):
    if c - a == 1:
        return X[a]
    assert X[a] == '[' and X[c - 1] == ']'
    b = a + 2
    nesting = 1 if X[a + 1] == '[' else 0
    while nesting > 0:
        if X[b] == '[':
            nesting += 1
        elif X[b] == ']':
            nesting -= 1
        b += 1
    #print(f'X[{a}:{c}]={X[a:c]}')
    #print('b', b)
    assert a + 1 < b and b < c - 1
    return 3 * magnitude(X, a + 1, b) + 2 * magnitude(X, b, c - 1)


def parse(s):
    s = s.replace(',', ' ')
    res = []
    i = 0
    while i < len(s):
        if s[i] in '[]':
            res.append(s[i])
        elif s[i] in digits:
            j = i + 1
            while s[j] in digits:
                j += 1
            res.append(int(s[i:j]))
            i = j - 1
        i += 1
    #print(res)
    return res


nums = []
for line in sys.stdin:
    nums.append(parse(line))

acc = nums[0]
for i in range(1, len(nums)):
    acc = add(acc, nums[i])
sys.stdout.write(f'ans {magnitude(acc, 0, len(acc))}\n')

ans2 = None
for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        s = add(nums[i], nums[j])
        x = magnitude(s, 0, len(s))
        if ans2 is None or ans2 < x:
            ans2 = x
sys.stdout.write(f'ans2 {ans2}\n')