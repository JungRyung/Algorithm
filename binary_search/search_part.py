N = int(input())
part = list(map(int, input().split()))
part.sort()

M = int(input())
search_part = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    else:
        return binary_search(array, target, mid + 1, end)

for p in search_part:
    result = binary_search(part, p, 0, N-1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")