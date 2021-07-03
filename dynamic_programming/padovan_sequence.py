##### 파도반 수열 #####
t = int(input())
for _ in range(t):
    n = int(input())
    seq = [1,1,1,2,2]
    if n<6:
        print(seq[n-1])
    else:
        for i in range(5,n):
            seq.append(seq[-5]+seq[-1])
        print(seq[n-1])