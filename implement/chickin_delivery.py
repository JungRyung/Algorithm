n, m = map(int, input().split())
city_map = [[] for _ in range(n)]
for i in range(n):
    city_map[i] = list(map(int, input().split()))

chickin_shops = []
homes = []
for i in range(n):
    for j in range(n):
        if city_map[i][j] == 2:
            chickin_shops.append((i,j))
        if city_map[i][j] == 1:
            homes.append((i,j))

# 각 치킨집에서 모든 집들까지의 거리를 구함
chickin_shop_dist = []
for chickin_shop in chickin_shops:
    dist_sum = 0
    for home in homes:
        dist_sum += abs(chickin_shop[0]-home[0]) + abs(chickin_shop[1]-home[1])
    chickin_shop_dist.append((dist_sum, (chickin_shop[0],chickin_shop[1])))

# 정렬하고 m개 까지만 자름
chickin_shop_dist.sort()
chickin_shop_results = chickin_shop_dist[:m]

# 도시의 치킨 거리 계산
chickin_dist = 0
for home in homes:
    min_dist = 1e9
    for chickin_shop in chickin_shop_results:
        tmp_dist = abs(chickin_shop[1][0]-home[0]) + abs(chickin_shop[1][1]-home[1])
        if tmp_dist < min_dist:
            min_dist = tmp_dist
    chickin_dist += min_dist

print(chickin_dist)