import sys
n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

searched = False
left = 0
right = n-1
while left<=right:
    mid = (left+right) // 2
    if numbers[mid] < mid:
        left = mid + 1
    elif numbers[mid] > mid:
        right = mid - 1
    else:
        print(mid)
        searched = True
        break

if searched ==False:
    print(-1)