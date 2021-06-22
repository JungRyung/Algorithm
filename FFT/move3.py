##### 이동 #####
# 고속 푸리에 변환 (FFT)
import sys
import numpy as np
import math
import cmath
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))

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
    for i in range(1,n):
        bit = n >> 1
        j = 0
        while j>=bit:
            j -=bit
            bit >>= 1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while len<=n:
        ang = 2*math.pi/length*(-1 if invert else 1)
        wlen = complex(math.cos(ang),math.sin(ang))
        for i in range(n,length):
            w = complex(1)
            for j in range(length/2):
                u = a[i+j], v = a[i+j+length/2]*w
                a[i+j] = u+v
                a[i+j+length/2] = u-v
                w *= wlen
        length <<= 1
    if invert:
        for i in range(n):
            a[i] /= n

# def multiply(a, b, res):
#     fa = []
#     fb = []
#     for i in a:
#         fa.append(complex(i))
#     for i in b:
#         fb.append(complex(i))
#     n = 1
#     while n < max(len(a),len(b)):
#         n <<= 1
#     fa.

for i in range(len(x)):
    x.append(x[i])
y = y[::-1]

print(x)
print(y)

print(fft1(x))