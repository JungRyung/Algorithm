# 감시 피하기 ulr: www.acmicpc.net/problem/18428
from itertools import combinations
import copy

n = int(input())
school_map = [[] for _ in range(n)]
blank_list = []
teacher_list = []

# map을 입력받고 공백과 선생님의 위치를 list에 정리
for i in range(n):
    school_map[i] = list(input().split())
    for j in range(n):
        if school_map[i][j] == 'X':
            blank_list.append((i,j))
        elif school_map[i][j] == 'T':
            teacher_list.append((i,j))
            
object_coms = list(combinations(blank_list,3))
def search_st(temp_map):
    for teacher in teacher_list:
        # 왼쪽 탐색
        nx = teacher[0]
        ny = teacher[1]
        while nx>=0 and temp_map[nx][ny]!='O':
            if temp_map[nx][ny] == 'S':
                return True
            nx -= 1
        # 오른쪽 탐색
        nx = teacher[0]
        ny = teacher[1]
        while nx<n and temp_map[nx][ny]!='O':
            if temp_map[nx][ny] == 'S':
                return True
            nx += 1
        # 위쪽 탐색
        nx = teacher[0]
        ny = teacher[1]
        while ny>=0 and temp_map[nx][ny]!='O':
            if temp_map[nx][ny] == 'S':
                return True
            ny -= 1
        # 아래쪽 탐색
        nx = teacher[0]
        ny = teacher[1]
        while ny<n and temp_map[nx][ny]!='O':
            if temp_map[nx][ny] == 'S':
                return True
            ny += 1
    return False

result = 'NO'
for object_com in object_coms:
    tmp_map = copy.deepcopy(school_map)
    for i in range(3):
        tmp_map[object_com[i][0]][object_com[i][1]] = 'O'
    if search_st(tmp_map) == False:
        result = 'YES'
        break
print(result)