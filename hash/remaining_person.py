'''
TITLE   : 회사에 있는 사람
URL     : https://www.acmicpc.net/problem/7785
DATE    : 21.11.06
'''
import sys

company = {}
n = int(sys.stdin.readline())

for _ in range(n):
    person, record = sys.stdin.readline().split()
    if record == "enter":
        company[person] = True
    else:
        company.pop(person)

company = list(company)
company.sort(reverse=True)
print('\n'.join(company))