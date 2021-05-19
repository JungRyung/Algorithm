##### 럭키 스트레이트 #####
num_int = int(input())
num_string = str(num_int)

left_sum = 0
right_sum = 0
idx = len(num_string)//2

for i in range(len(num_string)):
    if i < idx:
        left_sum += int(num_string[i])
    else:
        right_sum += int(num_string[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")