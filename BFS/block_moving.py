from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def get_next_pos(tmp_map,pos1,pos2):
    next_pos = []
    # 상하 좌우로 이동
    for i in range(4):
        nx1 = pos1[0] + dx[i]
        ny1 = pos1[1] + dy[i]
        nx2 = pos2[0] + dx[i]
        ny2 = pos2[1] + dy[i]
        if tmp_map[nx1][ny1]!=1 and tmp_map[nx2][ny2]!=1:
            next_pos.append(((nx1,ny1),(nx2,ny2)))
            # 둘다 비워져 있는 경우 -> 회전이 가능한 경우
            if tmp_map[nx1][ny1]==0 and tmp_map[nx2][ny2]==0:
                next_pos.append(((pos1[0],pos1[1]),(nx1,ny1)))
                next_pos.append(((pos2[0],pos2[1]),(nx2,ny2)))
    return next_pos
    
def solution(board):
    n = len(board)
    board.insert(0,[1]*(n+2))
    board.append([1]*(n+2))
    for i in range(n+2):
        board[i].insert(0,1)
        board[i].append(1)
    
    tmp_pos1 = (1,1)
    tmp_pos2 = (1,2)
    board[1][1] = 2
    board[1][2] = 2
    q = deque()
    visit = []
    q.append((tmp_pos1,tmp_pos2))
    visit.append(tmp_pos1)
    visit.append(tmp_pos2)
    while q:
        tmp_pos1, tmp_pos2 = q.popleft()
        for pos1, pos2 in get_next_pos(board,tmp_pos1,tmp_pos2):
            if 
        
    return answer

board = [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
answer = solution(board)
print(answer)