'''
TITLE   : 아스키 코드
URL     : https://www.acmicpc.net/problem/11654
DATE    : 21.07.30
'''
import sys

upper_cases = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_cases = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [i for i in range(10)]

char = sys.stdin.readline().strip()

if char in upper_cases:
    print(65 + upper_cases.index(char))
elif char in lower_cases:
    print(97 + lower_cases.index(char))
else:
    print(48 + numbers.index(int(char)))