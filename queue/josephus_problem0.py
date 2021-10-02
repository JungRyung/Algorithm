'''
TITLE   : 요세푸스 문제0
URL     : https://www.acmicpc.net/problem/11866
DATE    : 21.10.01
'''
import sys

n, k = map(int, sys.stdin.readline().split())

people = [i+1 for i in range(n)]
index = 0
ans = []
while len(people) > 0:
    for _ in range(k-1):
        index += 1
        if index >= len(people):
            index = 0
    ans.append(str(people.pop(index)))
    if index >= len(people):
        index = 0
        
print('<'+', '.join(ans)+'>')
