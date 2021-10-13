'''
TITLE   : 이중 우선순위 큐
URL     : https://www.acmicpc.net/problem/7662
DATE    : 21.10.12
'''
import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    min_heap = []
    max_heap = []
    min_del = []
    max_del = []
    n = int(sys.stdin.readline())
    for __ in range(n):
        command = list(sys.stdin.readline().split())
        # 삽입 연산
        if command[0] == 'I':
            heapq.heappush(min_heap, int(command[1]))
            heapq.heappush(max_heap, -int(command[1]))
        # 삭제 연산
        else:
            # 최대값 삭제
            if command[1] == '1':
                num = -max_heap[0]
                heapq.heappop(max_heap)
                if num in min_del:
                    min_del.remove(num)
                else:
                    max_del.append(num)
                    

            # 최소값 삭제
            else:
                num = min_heap[0]
                heapq.heappop(min_heap)
                if num in max_del:
                    max_del.remove(num)
                else:
                    min_del.append(num)
    print(min_heap)
    print(max_heap)
