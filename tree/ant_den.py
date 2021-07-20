'''
TITLE   : 개미굴
URL     : https://www.acmicpc.net/problem/14725
DATE    : 21.07.20
'''
import sys

n = int(sys.stdin.readline())
ants = [[] for _ in range(n)]
for i in range(n):
    ants[i] = list(sys.stdin.readline().split())[1:]

tree = {}
tree['root'] = []
for ant in ants:
    curr = 'root'
    for food in ant:
        if curr not in tree:
            tree[curr] = []
        if food not in tree[curr]:  
            tree[curr].append(food)
        curr = food
print(tree)
