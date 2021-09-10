'''
TITLE   : AC
URL     : https://www.acmicpc.net/problem/5430
DATE    : 21.09.09
'''
import sys

for _ in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    if n == 0:
        arr = []
    else:
        arr = sys.stdin.readline().strip()
        arr = arr[1:-1]
        arr = list(arr.split(','))
    print(arr)

    start = arr[0]