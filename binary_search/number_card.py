'''
TITLE   : 숫자 카드
URL     : https://www.acmicpc.net/problem/10815
DATE    : 23.04.23
'''
import sys

def binary_search(target: int, number_list: list, list_size: int) -> bool:
    start = 0
    end = list_size - 1

    while start <= end:
        mid = (start + end) // 2
        
        if number_list[mid] == target:
            return True
        elif number_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

n = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for number_m in m_list:
    if binary_search(number_m, n_list, n):
        print(1, end=" ")
    else:
        print(0, end=" ")
