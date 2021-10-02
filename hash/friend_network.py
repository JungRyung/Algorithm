'''
TITLE   : 친구 네트워크
URL     : https://www.acmicpc.net/problem/4195
DATE    : 21.10.01
'''
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:   
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(sys.stdin.readline())):
    f = int(sys.stdin.readline())
    friends = {}
    parent = [i for i in range(200000)]
    friends_set = [{i} for i in range(200000)]
    
    cnt = 0
    for __ in range(f):
        friendA, friendB = sys.stdin.readline().split()
        if friendA not in friends:
            friends[friendA] = cnt
            cnt += 1
        if friendB not in friends:
            friends[friendB] = cnt
            cnt += 1
        friendA_id = find_parent(parent, friends[friendA])
        friendB_id = find_parent(parent, friends[friendB])
        # 두 사람이 다른 집합에 속한 경우 -> union
        if find_parent(parent, friendA_id) != find_parent(parent, friendB_id):
            union_parent(parent, friendA_id, friendB_id)
            if friendA_id < friendB_id:
                friends_set[friendA_id] = friends_set[friendA_id] | friends_set[friendB_id]
            else:
                friends_set[friendB_id] = friends_set[friendA_id] | friends_set[friendB_id]
        if friendA_id < friendB_id:
            print(len(friends_set[friendA_id]))
        else:
            print(len(friends_set[friendB_id]))