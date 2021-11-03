'''
TITLE   : 베스트셀러
URL     : https://www.acmicpc.net/problem/1302
DATE    : 21.11.03
'''
import sys

n = int(sys.stdin.readline())
books = {}

for _ in  range(n):
    book = sys.stdin.readline().rstrip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

tuples = []
for book in books:
    tuples.append((-books[book], book))
    
tuples.sort()
print(tuples[0][1])