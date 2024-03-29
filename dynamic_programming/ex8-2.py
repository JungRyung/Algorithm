# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(n):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if n==1 or n==2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[n] != 0:
        return d[n]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]

n = int(input("피보나치 수열의 n번째 항을 구하고자 합니다. n을 입력해주세요 :"))
print(fibo(n))
