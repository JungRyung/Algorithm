def fFFT(L,w):
    l=len(L)
    if l==1:return [L[0]]
    R=[0]*l
    Even=fFFT(L[:l:2],w*w)
    Odd = fFFT(L[1:l:2],w*w)
    k=cx(1,0)
    for i in range(l//2):
        R[i]=Even[i]+k*Odd[i]
        R[i+l//2]=Even[i]-k*Odd[i]
        k*=w
    return R

def fConvolution(A,B):
    k=1
    while k<max(len(A),len(B))+1:k*=2
    k*=2
    if len(A)<k:A+=[0]*(k-len(A))
    if len(B)<k:B+=[0]*(k-len(B))
    w=cx(m.cos(2*m.pi/k),m.sin(2*m.pi/k))
    A=fFFT(A,w)
    B=fFFT(B,w)
    C=[A[i]*B[i] for i in range(k)]
    C=fFFT(C,cx(1, 0)/w)
    for i in range(k):
        C[i]/=cx(k,0)
        C[i]=cx(round(C[i].real), round(C[i].imag))
    return C

import math as m
cx=complex
n=int(input())
A=[*map(int,input().split())]*2
B=[*map(int,input().split())][::-1]
R=fConvolution(A,B)
r=0
for i in range(n-1,2*n-1):r=max(r,R[i].real)
print(int(r))