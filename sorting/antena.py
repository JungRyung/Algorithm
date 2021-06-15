n = int(input())
homes = list(map(int,input().split()))

dist = []
for i in range(n):
    dist.append([0,homes[i]])
for i in range(n):
    for j in range(i,n):
        tmp_dist = abs(homes[i] - homes[j])
        dist[i][0] += tmp_dist
        dist[j][0] += tmp_dist

dist.sort()

answer = dist[0][1]
print(answer)