import math

def time_to_min(time):
    hh, mm = map(int, time.split(':'))
    return hh * 60 + mm
    
def cal_time(in_time, out_time):
    in_time = time_to_min(in_time)
    out_time = time_to_min(out_time)
    return out_time - in_time

def cal_fee(time,fees):
    fee = fees[1]
    if time > fees[0]:
        fee += math.ceil((time - fees[0]) / fees[2]) * fees[3]
    return fee

def solution(fees, records):
    answer = []
    cars = []
    car_times = {}
    for record in records:
        time, car_number, io = record.split()
        if car_number not in cars:
            cars.append(car_number)
            car_times[car_number] = []
        car_times[car_number].append(time)
    cars.sort()
    for car in cars:
        if len(car_times[car]) % 2 == 1:
            car_times[car].append("23:59")
        total_time = 0
        for i in range(len(car_times[car]) // 2):
            total_time += cal_time(car_times[car][2*i],car_times[car][2*i+1])
        answer.append(cal_fee(total_time,fees))
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result = solution(fees, records)
print(result)