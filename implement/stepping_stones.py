'''
TITLE   : 니니즈 친구들 징검다리 건너기
DATE    : 21.10.28
'''
# 이진탐색
def is_possible(stones, k, mid):
    stones_len = len(stones)
    i = 0
    skip = 0
    while True:
        if i >= stones_len:
            if skip >= k:
                return False
            else:
                return True
            
        if stones[i] > mid-1:
            skip = 0
            i += 1
        else:
            if skip < k-1:
                skip += 1
                i += 1
            else:
                return False
def solution(stones, k):
    answer = 0
    right = max(stones)
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if is_possible(stones[:], k, mid):
            answer = max(answer,mid)
            left = mid+1
        else:
            right = mid-1
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

ans = solution(stones, k)
print(ans)