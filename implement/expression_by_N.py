##### N으로 표현 #####
# URL : https://programmers.co.kr/learn/courses/30/lessons/42895
def solution(N, number):
    answer = 0
    if N == number:
        return 1
    # N의 개수가 i개일 때 만들 수 있는 모든 수를 포함한 리스트
    dp = [0,[N]]    # N이 1개일 때는 이미 만들어 둔다.
    for i in range(2,9):
        tmp = []
        # N을 겹친 수 추가
        tmp.append(int(str(N)*i))
        half_num = i//2+1
        for idx in range(1,half_num):
            for x in dp[idx]:
                for y in dp[i-idx]: 
                    tmp.append(x + y)
                    tmp.append(x * y)
                    if x - y >= 0:
                        tmp.append(x - y)
                    if y - x >= 0:
                        tmp.append(x - y)
                    if y > 0:
                        tmp.append(x/y)
                    if x > 0:
                        tmp.append(y/x)
        if number in tmp:
            return i
        dp.append(tmp)
        print(tmp)
    return -1

n, num = map(int, input().split())
answer = solution(n,num)
print(answer)

