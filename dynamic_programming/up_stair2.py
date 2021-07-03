import sys
n = int(input())
a = list(map(int, sys.stdin.readlines())) + [0]
print(a)
x = [0] * (n + 1)
for i in range(n):
  x[i] = a[i] + max(x[max(i - 2, -1)],
                    x[max(i - 3, -1)] + a[max(i - 1, -1)])
print(x[n - 1])