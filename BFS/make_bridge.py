'''
TITLE   : 다리 만들기
URL     : https://www.acmicpc.net/problem/2146
DATE    : 21.08.13
'''
import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n = int(sys.stdin.readline())
islands_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]