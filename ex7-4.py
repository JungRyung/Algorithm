# 빠르게 입력받기위해 readline()사용
import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rsplit()

# 입력받은 문자열 그대로 출력
print(input_data)