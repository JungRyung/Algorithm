n,x = map(int,input().split())
numbers = list(map(int,input().split()))

cnt = 0
while numbers:
    searched = False
    left = 0
    right = n-1
    while left<=right:
        mid = (left+right) // 2
        if numbers[mid] == x:
            cnt += 1
            numbers.pop(mid)
            n -= 1
            searched = True
        elif numbers[mid]<x:
            left = mid+1
        else:
            right = mid-1
    if searched == False:
        break
if cnt>0:
    print(cnt)
else:
    print(-1)