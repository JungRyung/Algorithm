##### 이동 #####
# 고속 푸리에 변환 (FFT)
import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))

def get_score(x,y):
    sum = 0
    for i in range(n):
        tmp_mul = x[i]*y[i]
        sum += tmp_mul
    return sum

def move(arr,num):
    for _ in range(num):
        tmp = arr.pop(-1)
        arr.insert(0,tmp)
    return arr

max_score = 0
for i in range(n):
    x = move(x,1)
    max_score = max(max_score, get_score(x,y))
print(max_score)
        