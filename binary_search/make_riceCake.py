N, M = map(int, input().split())

length = list(map(int, input().split()))

length.sort(reverse=True)

start = 0
end = length[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in length:
        if i > mid:
            sum += (i - mid)
        else:
            break
    if sum >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
    