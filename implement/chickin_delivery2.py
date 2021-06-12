from itertools import combinations
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

# m개의 치킨집을 뽑는 모든 조합
chickin_combinations = list(combinations(chickin_shops, m))

min_chickin_dist = 1e9
for chickins in chickin_combinations:
    chickin_dist = 0
    for home in homes:
        tmp_dist = 1e9
        for chickin in chickins:
            tmp_dist = min(tmp_dist, abs(chickin[0]-home[0])+abs(chickin[1]-home[1]))
        chickin_dist += tmp_dist
    min_chickin_dist = min(min_chickin_dist, chickin_dist)

print(min_chickin_dist)