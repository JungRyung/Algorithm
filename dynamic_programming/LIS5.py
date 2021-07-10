##### 가장 긴 증가하는 부분 수열 5 #####
# URL : https://www.acmicpc.net/problem/14003
import sys
import bisect

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

lis = [seq[0]]
ans = [(0,seq[0])]
for num in seq:
    if num > lis[-1]:
        lis.append(num)
        ans.append((len(lis)-1,num))
    elif num < lis[-1]:
        lis[bisect.bisect_left(lis,num)] = num
        ans.append((bisect.bisect_left(lis,num),num))
s = []
idx = len(lis)
for tmp in ans[::-1]:
    tmp_idx, tmp_num = tmp
    if tmp_idx == idx-1:
        s.append(tmp_num)
        idx -= 1
print(ans)
print(len(s))
print(*s[::-1])