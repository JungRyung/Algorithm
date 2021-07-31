'''
TITLE   : 광고 삽입
URL     : https://programmers.co.kr/learn/courses/30/lessons/72414
DATE    : 21.07.30
'''

def time_to_sec(time):
    hh, mm, ss = map(int, time.split(':'))
    sec = 0
    sec += hh * 3600
    sec += mm * 60
    sec += ss
    return sec

def sec_to_time(sec):
    hh = sec // 3600
    sec %= 3600
    mm = sec // 60
    sec %= 60
    ss = sec
    return "%02d:%02d:%02d" % (hh,mm,ss)
    
def solution(play_time, adv_time, logs):
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    temp_view = [0] * play_time

    for log in logs:
        adv_start, adv_end = log.split('-')
        adv_start = time_to_sec(adv_start)
        adv_end = time_to_sec(adv_end)
        temp_view[adv_start] += 1
        if adv_end < play_time:
            temp_view[adv_end] -= 1
    
    atom = 0
    for i in range(play_time):
        atom += temp_view[i]
        temp_view[i] = atom

    accum_view = [0] * play_time
    accum_view[0] = temp_view[0]
    for i in range(1,play_time):
        accum_view[i] = accum_view[i-1] + temp_view[i]

    max_view = 0
    sec = 0
    for i in range(play_time-adv_time+1):
        if i == 0:
             range_view = accum_view[i+adv_time-1] - 0
        else:
            range_view = accum_view[i+adv_time-1] - accum_view[i-1]
        if range_view > max_view:
            max_view = range_view
            sec = i
    
    return sec_to_time(sec)

play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

answer = solution(play_time, adv_time, logs)
print(answer)