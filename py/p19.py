#!/usr/bin/env python3

from collections import defaultdict, deque
import sys

input = [x.strip() for x in sys.stdin.readlines()]
scanners = []
i = -1
while i < len(input):
    j = i + 2
    while j < len(input) and input[j]:
        j += 1
    S = []
    for l in input[i + 2:j]:
        [x, y, z] = l.split(',')
        S.append((int(x), int(y), int(z)))
    scanners.append(S)
    i = j
input = None


def dot(X, Y):
    return sum(X[i] * Y[i] for i in range(3))


def cross(X, Y):
    return (X[1] * Y[2] - X[2] * Y[1], X[2] * Y[0] - X[0] * Y[2],
            X[0] * Y[1] - X[1] * Y[0])


D = []
units = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
for u in units:
    for v in units:
        if dot(u, v) != 0:
            continue
        w = cross(u, v)
        D.append([u, v, w])
assert len(D) == 24

print(D[:2])


def C(d, si, pi, i):
    return dot(scanners[si][pi], D[d][i])


scnt = len(scanners)

beacon = [None for _ in range(scnt)]
fixed = [False for _ in range(scnt)]
todo = deque()

beacon[0] = (0, 0, 0)
fixed[0] = True
todo.append(0)

while todo:
    sj = todo.popleft()
    sjcnt = len(scanners[sj])
    pjs = set(
        (C(0, sj, j, 0), C(0, sj, j, 1), C(0, sj, j, 2)) for j in range(sjcnt))
    print(f'sj={sj}')
    for si in range(scnt):
        if fixed[si]:
            continue
        print(f'si={si}')
        for d in range(24):
            sicnt = len(scanners[si])
            deltas = defaultdict(int)
            for i in range(sicnt):
                for j in range(sjcnt):
                    dx = C(0, sj, j, 0) - C(d, si, i, 0)
                    dy = C(0, sj, j, 1) - C(d, si, i, 1)
                    dz = C(0, sj, j, 2) - C(d, si, i, 2)
                    deltas[(dx, dy, dz)] += 1
            deltas = sorted((-c, d) for d, c in deltas.items() if c >= 12)
            common = 0
            for _, (dx, dy, dz) in deltas:
                common = 0
                newsi = []
                for ii in range(sicnt):
                    x = C(d, si, ii, 0) + dx
                    y = C(d, si, ii, 1) + dy
                    z = C(d, si, ii, 2) + dz
                    newsi.append((x, y, z))
                    if (x, y, z) in pjs:
                        common += 1
                if common >= 12:
                    print(
                        f'overlap {si} and {sj}: shift ({dx},{dy},{dz}) orient {D[d]}'
                    )
                    beacon[si] = (dx, dy, dz)
                    scanners[si] = newsi
                    fixed[si] = True
                    todo.append(si)
                    break
            if common >= 12:
                break

# Now put all in one set and count
allPs = set()
for S in scanners:
    for P in S:
        allPs.add(P)
sys.stdout.write(f'ans {len(allPs)}\n')

print(beacon)
bigd = None
for j in range(scnt):
    for i in range(j):
        d = sum(abs(beacon[i][k] - beacon[j][k]) for k in range(3))
        if bigd is None or bigd < d:
            bigd = d
sys.stdout.write(f'bigd {bigd}\n')