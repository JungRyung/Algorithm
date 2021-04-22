def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input("피보나치 수열의 n번째 항을 구하고자 합니다. n을 입력해주세요 :"))
print(fibo(n))