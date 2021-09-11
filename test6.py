def attack(board, x1,y1,x2,y2,amount):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            board[i][j] -= amount
def heal(board, x1,y1,x2,y2,amount):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            board[i][j] += amount
def count_building(board):
    cnt = 0
    r = len(board)
    c = len(board[0])
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                cnt += 1
    return cnt

def solution(board, skill):
    answer = 0
    r = len(board)
    c = len(board[0])
    dp = [[0]*c for _ in range(r)]
    for command in skill:
        print(command)
        type, r1, c1, r2, c2, degree = command
        r3, c3 = r1, c2
        r4, c4 = r2, c1
        if type == 1:
            dp[r1][c1] -= degree
            if c3+1 < c:
                dp[r3][c3+1] += degree
            dp[r4][c4] -= degree
            if c2+1 < c:
                dp[r2][c2+1] += degree
        elif type == 2:
            dp[r1][c1] += degree
            if c3 < c:
                dp[r3][c3] -= degree
            dp[r4][c4] += degree
            if c2 < c:
                dp[r2][c2] -= degree
    print(dp)
    for i in range(r):
        rate = 0
        for j in range(c):
            rate += dp[i][j]
            board[i][j] += rate
            if board[i][j] > 0:
                answer += 1
        
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

result = solution(board, skill)
print(result)