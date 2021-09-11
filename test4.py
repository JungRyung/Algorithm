from itertools import combinations_with_replacement
INF = 10e9

def comparison_scores(ryan, apeach):
    apeach_score = 0
    ryan_score = 0
    for i in range(11):
        tmp_score = 10 - i
        ryan_cnt = ryan[i]
        apeach_cnt = apeach[i]
        if ryan_cnt > 0 or apeach_cnt > 0:
            if apeach_cnt >= ryan_cnt:
                apeach_score += tmp_score
            else:
                ryan_score += tmp_score
        
    return ryan_score - apeach_score

def make_ryans(n):
    items = [0,1,2,3,4,5,6,7,8,9,10]
    scores = []
    for cwr in combinations_with_replacement(items,n):
        score = [0]*11
        for i in cwr:
            score[i] += 1
        scores.append(score)
    return scores

def solution(n, info):
    answers = []
    ryans = make_ryans(n)
    
    max_score = -INF
    for ryan in ryans:
        score_diff = comparison_scores(ryan, info)
        if max_score < score_diff:
            max_score = score_diff
            answers = []
            answers.append(ryan[::-1])
        elif max_score == score_diff:
            answers.append(ryan[::-1])
    answers.sort()
    if max_score > 0:
        answer = answers[-1][::-1]
    else:
        answer = [-1]
    return answer

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]

result = solution(n, info)
print(result)
