##### 자물쇠와 열쇠 #####
# URL : https://programmers.co.kr/learn/courses/30/lessons/60059
def padding_lock(lock):
    n = len(lock)
    padded_lock = [[0]*(3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                padded_lock[n+i][n+j] = 1
    return padded_lock

def rotate_90(key):
    m = len(key)
    ret = [[0] * m for _ in range(m)]

    for row in range(m):
        for col in range(m):
            ret[col][m-1-row] = key[row][col]
    return ret

def check(padded_lock):
    n = len(padded_lock) // 3
    for i in range(n,2*n):
        for j in range(n,2*n):
            if padded_lock != 1:
                return False
    return True

def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    # lock을 패딩하기
    padded_lock = padding_lock(lock)

    # 패딩한 lock에 회전하고 이동시킨 key를 합치기
    for _ in range(4):
        key = rotate_90(key)
        for x in range(2*n):
            for y in range(2*n):
                for i in range(m):
                    for j in range(m):
                        padded_lock[x+i][y+j] += key[i][j]
                if check(padded_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        padded_lock[x+i][y+j] -= key[i][j]
    return False
            

    # for _ in range(3):
    #     for i in range(-M+1,M):
    #         for j in range(-M+1,M):
    #             if rev_lock == padding_move(key,i,j):
    #                 answer = True
    #                 break
    #         if answer == True:
    #             break
    #     key = rotate_90(key)

    # return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
key_90_turn = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

answer = solution(key, lock)
print(answer)