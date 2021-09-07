'''
TITLE   : 음계
URL     : https://www.acmicpc.net/problem/2920
DATE    : 21.09.07
'''
import sys

notes = list(map(int, sys.stdin.readline().split()))

before = notes[0]
check = [0,0]
for note in notes:
    if note < before:
        check[0] = 1
    elif note > before:
        check[1] = 1
    before = note
if check[0]==1 and check[1]==1:
    print("mixed")
elif check[0]==1 and check[1]==0:
    print("descending")
elif check[0]==0 and check[1]==1:
    print("ascending")