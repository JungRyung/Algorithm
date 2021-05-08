# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 학생의 수와 연산의 수를 입력받기
v, n = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 결과를 담을 리스트 선언
result = []

# 입력에 따라 연산 진행
for i in range(n):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union_parent(parent, a, b)
    elif cal == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")

for i in result:
    print(i)