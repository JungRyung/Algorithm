'''
TITLE   : 사분면 고르기
URL     : https://www.acmicpc.net/problem/14681
DATE    : 21.09.06
'''
x = int(input())
y = int(input())
if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)