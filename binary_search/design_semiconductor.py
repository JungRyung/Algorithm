'''
TITLE   : 반도체 설계
URL     : https://www.acmicpc.net/problem/2352
DATE    : 21.07.29
'''
import sys
import bisect

n = int(sys.stdin.readline())
ports = list(map(int, sys.stdin.readline().split()))

lis = []
lis.append(ports[0])

for port in ports:
    if port < lis[-1]:
        lis[bisect.bisect_left(lis, port)] = port
    elif port > lis[-1]:
        lis.append(port)
print(len(lis))