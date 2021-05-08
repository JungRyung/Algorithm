# 도시 분할 계획 -> kruskal 알고리즘

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집의 개수와 길의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 모든 길에 대한 정보를 입력받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 최소 신장트리로 만든 다음 가장 큰 비용을 가진 길을 제거 -> 최적의 마을 두개로 나뉠 수 있음
result = 0
max_cost = 0
# 1) 최소신장 트리 구성
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = cost

# 2) 최소 비용 계산
print(result - max_cost)