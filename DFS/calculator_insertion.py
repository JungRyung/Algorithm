min_result = 1e9
max_result = -1e9

n = int(input())
number = list(map(int,input().split()))
sum, sub, mul, div = map(int,input().split())

graph = [[] for _ in range(n-1)]
cal = number[0]
def dfs(i, cal):
    global min_result, max_result, sum, sub, mul, div
    if i == n:
        min_result = min(min_result, cal)
        max_result = max(max_result, cal)
    else:# + 노드
        if sum > 0:
            sum -= 1
            dfs(i+1, cal+number[i])
            sum += 1
        # - 노드
        if sub > 0:
            sub -= 1
            dfs(i+1, cal-number[i])
            sub += 1
        # * 노드
        if mul > 0:
            mul -= 1
            dfs(i+1, cal*number[i])
            mul += 1
        # / 노드
        if div > 0:
            div -= 1
            dfs(i+1, int(cal/number[i]))
            div += 1
            
dfs(1, cal)

print(max_result)
print(min_result)