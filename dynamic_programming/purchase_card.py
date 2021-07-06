##### 카드 구매하기 #####
# URL : https://www.acmicpc.net/problem/11052
n = int(input())
cards = [0] + list(map(int ,input().split()))

da = [0] * (n+1)

for i in range(1,n+1):
    for j in range(i,0,-1):
        if j==i:
            da[i] = max(da[i],cards[j])
        else:
            da[i] = max(da[i],cards[j]+da[i-j])
print(da[n])