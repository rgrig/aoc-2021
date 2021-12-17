#!/usr/bin/env python3

import sys

INF = 10000  #hack:(

total_ver = 0


def eval(start, packets, bits):
    global total_ver
    #print(start, packets, bits)
    result = []
    while packets > 0 and start < len(bits):
        version = int(bits[start:start + 3], 2)
        total_ver += version
        #print(version)
        typ = int(bits[start + 3:start + 6], 2)
        if typ == 4:
            #print('lit')
            i = start + 6
            value = 0
            while bits[i] == '1':
                value = 16 * value + int(bits[i + 1:i + 5], 2)
                i += 5
            value = 16 * value + int(bits[i + 1:i + 5], 2)
            result.append(value)
            packets -= 1
            start = i + 5
        else:
            subvalues = None
            if bits[start + 6] == '0':
                #print('op0')
                sublen = int(bits[start + 7:start + 7 + 15], 2)
                _, subvalues = eval(
                    0, INF, bits[start + 7 + 15:start + 7 + 15 + sublen])
                packets -= 1
                start += 7 + 15 + sublen
            else:
                #print('op1')
                subcnt = int(bits[start + 7:start + 7 + 11], 2)
                start, subvalues = eval(start + 7 + 11, subcnt, bits)
                packets -= 1
            assert subvalues is not None
            if typ == 0:
                result.append(sum(subvalues))
            elif typ == 1:
                r = 1
                for v in subvalues:
                    r *= v
                result.append(r)
            elif typ == 2:
                result.append(min(subvalues))
            elif typ == 3:
                result.append(max(subvalues))
            elif typ == 5:
                result.append(1 if subvalues[0] > subvalues[1] else 0)
            elif typ == 6:
                result.append(1 if subvalues[0] < subvalues[1] else 0)
            elif typ == 7:
                result.append(1 if subvalues[0] == subvalues[1] else 0)
    return (start, result)


def solve(packet):
    global total_ver
    bits = []
    for c in packet:
        bits.extend('{:04b}'.format(int(c, 16)))
    bits = ''.join(bits)
    #print('START')
    total_ver = 0
    _, vs = eval(0, 1, bits)
    sys.stdout.write(f'total_ver {total_ver}  values {vs}\n')


for line in sys.stdin:
    solve(line.strip())