def padding_move(key,hor,ver):
    M = len(key)
    # M-1 만큼 패딩한 배열 만들기
    padd_len = 3*M
    ret = [[0] * padd_len for _ in range(padd_len)]
    ret_ = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            ret[M+i+ver][M+j+hor] = key[i][j]

    # 패딩 제거
    for i in range(M):
        ret_[i] = ret[M+i][M:2*M]
    return ret_

"""
def padding_move_numpy(key,hor,ver):
    M = len(key)
    # M-1 만큼 패딩한 배열 만들기
    padd_len = 3*M - 2
    ret = np.array(key)
    ret = np.pad(ret, ((M-1,M-1),(M-1,M-1)))
    print(ret)
    
    # for i in range(M):
    #     for j in range(M):
    #         ret[i+ver][j+hor] = key[i][j]

    # # 패딩 제거
    # print(ret)
    # print(ret[M-1:2*M-1,M-1:2*M-1])

def horizontal_move(key,step):
    M = len(key)
    ret = [[0] * M for _ in range(M)]
    

def move_right(key,step):
    M = len(key)
    ret = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M-step):
            ret[i][j+step] = key[i][j]
    return ret

def move_left(key,step):
    M = len(key)
    ret = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(step,M):
            ret[i][j-step] = key[i][j]
    return ret

def move_up(key,step):
    M = len(key)
    ret = [[0] * M for _ in range(M)]
    for i in range(step,M):
        for j in range(M):
            ret[i-step][j] = key[i][j]
    return ret

def move_down(key,step):
    M = len(key)
    ret = [[0] * M for _ in range(M)]
    for i in range(M-step):
        for j in range(M):
            ret[i+step][j] = key[i][j]
    return ret
"""

def rotate_90(key):
    N = len(key)
    ret = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            ret[col][N-1-row] = key[row][col]
    return ret
    

def solution(key, lock):
    answer = False
    M = len(key)
    rev_lock = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            if lock[i][j] == 1:
                rev_lock[i][j] = 0
            else:
                rev_lock[i][j] = 1

    for _ in range(3):
        for i in range(-M+1,M):
            for j in range(-M+1,M):
                if rev_lock == padding_move(key,i,j):
                    answer = True
                    break
            if answer == True:
                break
        key = rotate_90(key)

    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
key_90_turn = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

answer = solution(key, lock)
print(answer)