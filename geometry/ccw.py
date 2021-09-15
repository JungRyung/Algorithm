'''
TITLE   : CCW
URL     : https://www.acmicpc.net/problem/11758
DATE    : 21.09.14
'''
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

vector_1to2 = (x2-x1, y2-y1)
vector_1to3 = (x3-x1, y3-y1)

# 외적
outer_product = vector_1to2[0]*vector_1to3[1] - vector_1to2[1]*vector_1to3[0]

if outer_product > 0:
    print(1)
elif outer_product < 0:
    print(-1)
else:
    print(0)