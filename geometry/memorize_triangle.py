'''
TITLE   : 삼각형 외우기
URL     : https://www.acmicpc.net/problem/10101
DATE    : 21.09.14
'''
sides = [int(input()) for _ in range(3)]

if sides[0]==60 and sides[1]==60 and sides[2]==60:
    print("Equilateral")
elif sum(sides)==180:
    if sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")