'''
TITLE   : 나는야 포켓몬 마스터 이다솜
URL     : https://www.acmicpc.net/problem/1620
DATE    : 21.10.01
'''
import sys

n, m = map(int, sys.stdin.readline().split())

num_to_name = {}
name_to_num = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    num_to_name[i+1] = name
    name_to_num[name] = i+1

for _ in range(m):
    question = sys.stdin.readline().strip()
    # 숫자일 때
    if ord('0')<=ord(question[0])<=ord('9'):
        print(num_to_name[int(question)])
    # 이름일 때
    else:
        print(name_to_num[question])