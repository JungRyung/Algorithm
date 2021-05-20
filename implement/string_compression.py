def solution(s):
    answer = 0
    min_len = 1001
    for i in range(1,len(s)//2 + 1):
        tmp = s[:i]
        idx = i
        cnt = 1
        result = ''
        while idx < len(s):
            if s[idx:idx+i] == tmp:
                cnt += 1
                idx += i
            else:
                if cnt > 1:
                    result += str(cnt)
                result += tmp
                tmp = s[idx:idx+i]
                cnt = 1
                idx += i
        if cnt > 1:
            result += str(cnt)
        result += tmp
        if len(result) < min_len:
            min_len = len(result)
    answer = min_len
    if len(s) == 1:
        answer = 1
    return answer

s = ""
answer = solution(s)
print(answer)