##### 설탕 배달 #####
# URL : https://www.acmicpc.net/problem/2839
n = int(input())
# 입력값을 18이라 가정

# 5킬로그램 봉지개수를 최대로 하고 줄여나가는 방식으로 계산
# n이 5로 나누어 떨어지면 5킬로그램 봉지만으로 구성한 봉지수가 최소값
if n % 5 == 0:
    print(n//5)
else:
    answer = 0
    cnt = n // 5
    while cnt >=0:
        if (n - cnt * 5) % 3 ==0:
            answer = cnt + ((n - cnt * 5) // 3)
            break
        else:
            cnt -= 1
    
    if answer!= 0:
        print(answer)
    else:
        print(-1)