'''
TITLE   : 택시 기하학
URL     : https://www.acmicpc.net/problem/3053
DATE    : 21.09.14
'''
import math
r = int(input())
area_of_circle = r**2 * math.pi
print("%.6f"%area_of_circle)
taxi_area = (r**2 + r**2)
print("%.6f"%taxi_area)