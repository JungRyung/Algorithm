##### 피보나치 재귀함수의 0 또는 1 출력 횟수 구하기 #####
# URL : https://www.acmicpc.net/problem/1003
t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else:
        da = [0]*(n+1)
        da[0] = (1,0)
        da[1] = (0,1)
        for i in range(2,n+1):
            cnt_0 = da[i-1][0] + da[i-2][0]
            cnt_1 = da[i-1][1] + da[i-2][1]
            da[i] = (cnt_0, cnt_1)
        print('{} {}'.format(da[n][0],da[n][1]))