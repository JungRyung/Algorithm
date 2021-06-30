##### 정수 삼각형 ####
# URL : https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
def solution(triangle):
    answer = 0
    length = len(triangle)
    
    if length == 1:
        return triangle[0][0]
    da = [[0]*(i+1) for i in range(length)]
    da[0][0] = triangle[0][0]

    for i in range(1,length):
        for j in range(len(triangle[i])):
            # left
            if j>0:
                left = da[i-1][j-1]
            else:
                left = 0
            # right
            if j != len(triangle[i])-1:
                right = da[i-1][j]
            else:
                right = 0
            da[i][j] = max(left,right) + triangle[i][j]
    answer = max(da[length-1])

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
answer = solution(triangle)
print(answer)