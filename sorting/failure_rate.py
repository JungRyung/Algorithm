def solution(N, stages):
    answer = []
    clear = [0 for _ in range(N+1)]
    failure_rate = []

    for stage in stages:
        for i in range(stage):
            clear[i] += 1

    for i in range(N):
        if clear[i] == 0:
            failure_rate.append((0,i+1))
        else:
            failure_rate.append(((clear[i]-clear[i+1])/clear[i],i+1))
    
    failure_rate.sort(key = lambda x : (-x[0],x[1]))
    
    for i in range(N):
        answer.append(failure_rate[i][1])
    return answer