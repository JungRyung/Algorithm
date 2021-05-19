##### 문자열 뒤집기 #####
S = input()
cnt = 0
tmp = S[0]
for i in S:
    if i != tmp:
        cnt += 1

reverse_num = cnt//2
if cnt%2 >0:
    reverse_num +=1

print(reverse_num)