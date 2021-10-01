##### 이동 #####
# 고속 푸리에 변환 (FFT)
import sys
# import numpy as np
import math
import cmath
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))
def resize(arr,n):
    if len(arr) < n:
        t = n - len(arr)
        for i in range(t):
            arr.append(0)
    elif len(arr) > n:
        t = len(arr) - n
        for i in range(t):
            arr.pop(-1)
    return arr

def omega(p, q):
  return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

def fft1(signal):
  n = len(signal)
  if n == 1:
     return signal
  else:
     Feven = fft1([signal[i] for i in range(0, n, 2)])
     Fodd = fft1([signal[i] for i in range(1, n, 2)])
     combined = [0] * n
     for m in range(n // 2):
        combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
        combined[m + n // 2] = Feven[m] - omega(n, -m) * Fodd[m]
     return combined
     
def fft(a, invert):
    n = len(a)
    j = 0
    for i in range(1,n):
        bit = n >> 1
        while j>=bit:
            j -=bit
            bit >>= 1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length<=n:
        ang = 2*math.pi/length*(-1 if invert else 1)
        wlen = complex(math.cos(ang),math.sin(ang))
        for i in range(0,n,length):
            w = complex(1)
            k = 0
            while k<length/2:
                u = a[i+k]
                v = a[i+k+length//2]*w
                a[i+k] = u+v
                a[i+k+length//2] = u-v
                w *= wlen
                k += 1
        length <<= 1
    if invert:
        for i in range(n):
            a[i] /= n
    return a

def multiply(a, b):
    n = 1
    while n < max(len(a),len(b)):
        n <<= 1
    a = resize(a,n)
    b = resize(b,n)
    fa = []
    fb = []
    for i in a:
        fa.append(complex(i))
    for i in b:
        fb.append(complex(i))
    fa = fft(fa,False)
    fb = fft(fb,False)
    for i in range(n):
        fa[i] *= fb[i]
    fft(fa,True)
    res = []
    for i in range(n):
        res.append(int(fa[i].real + (0.5 if fa[i].real>0 else -0.5)))
    return res

for i in range(len(x)):
    x.append(x[i])
y = y[::-1]

res = multiply(x,y)
ans = 0
for i in range(n,n*2):
    ans = max(ans, res[i])

print(ans)