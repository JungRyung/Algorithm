##### 팰린드롬 수 #####
# URL : https://www.acmicpc.net/problem/1259
import sys

while True:
    num = int(sys.stdin.readline())
    num_list = []
    if num != 0:
        while num>0:
            tmp = num % 10
            num_list.append(tmp)
            num //= 10
        if num_list == num_list[::-1]:
            print("yes")
        else:
            print("no")
    else:
        break