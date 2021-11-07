'''
TITLE   : 암기왕
URL     : https://www.acmicpc.net/problem/2776
DATE    : 21.11.07
'''
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    note1 = list(map(int, sys.stdin.readline().split()))
    note1_dict = {}
    for num in note1:
        note1_dict[num] = True
    m = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))
    ans = []
    for num in note2:
        if num in note1_dict:
            ans.append('1')
        else:
            ans.append('0')

    print('\n'.join(ans))
