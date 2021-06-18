##### 병사 배치하기 ######
# LIS(Longest Increasing Subsequence) -> 재귀함수로 구현(DP 포함)
import sys

def lds(arr):
    arr = [1e9] + arr
    N = len(arr)
    cache = [-1] * N

    def find(start):
        if cache[start] != -1:
            return cache[start]

        ret = 0
        for nxt in range(start+1, N):
            if arr[start] > arr[nxt]:
                ret = max(ret, find(nxt) + 1)
        
        cache[start] = ret
        return ret
    
    return find(0)

n = int(sys.stdin.readline())
soldiers = list(map(int,sys.stdin.readline().split()))

lds_num = lds(soldiers)

answer = n - lds_num
print(answer)