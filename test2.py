import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def n_to_k(n,k):
    result = ''
    while n > 0:
        result += str(n % k)
        n //= k
    return result[::-1]

def solution(n, k):
    answer = 0
    n = n_to_k(n,k)
    numbers = list(n.split('0'))

    for number in numbers:
        if number == '':
            number = 0
        else:
            number = int(number)
        if is_prime(number):
            answer += 1

    return answer

n = 110011
k = 10

result = solution(n, k)
print(result)
