def solution(id_list, report, k):
    answer = []
    report = set(report)
    report_dic = {}
    reported = {}
    for id in id_list:
        report_dic[id] = []
        reported[id] = k
    for repo in report:
        a, b = repo.split()
        report_dic[a].append(b)
        reported[b] -= 1
    for id in id_list:
        cnt = 0
        for b in report_dic[id]:
            if reported[b] <= 0:
                cnt += 1
        answer.append(cnt)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

result = solution(id_list, report, k)
print(result)