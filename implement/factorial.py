##### 팩토리얼 #####
# URL : https://www.acmicpc.net/problem/10872
n = int(input())

def facto(num):
    if num == 1 or num == 0:
        return 1
    return num*facto(num-1)

answer = facto(n)
print(answer)