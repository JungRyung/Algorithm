'''
TITLE   : 2007년
URL     : https://www.acmicpc.net/problem/1924
DATE    : 21.09.06
'''
x, y = map(int, input().split())
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
mon = [31,28,31,30,31,30,31,31,30,31,30,31]
offset = 0

sum = 0
for i in range(0,x-1):
    sum += mon[i]
sum += y
print(week[(offset + sum)%7])