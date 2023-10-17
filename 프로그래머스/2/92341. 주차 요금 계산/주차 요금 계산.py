from math import ceil
from collections import defaultdict

def solution(fees, records):
    parking = defaultdict(list)  
    total_time = defaultdict(int)  

    for record in records:
        time, car_num, status = record.split()
        hour, minute = map(int, time.split(':'))
        total_minute = hour * 60 + minute  

        if status == 'IN':
            parking[car_num].append(total_minute)
        elif status == 'OUT':
            in_time = parking[car_num].pop()  # 마지막 입차 시간
            total_time[car_num] += total_minute - in_time  # 주차 시간 누적

    # 23:59에 출차 처리
    for car_num, times in parking.items():
        if times:  # 출차되지 않은 차량이 있는 경우
            total_time[car_num] += 1439 - times.pop()  # 23:59에 출차 처리

    # 주차 요금 계산
    base_time, base_fee, unit_time, unit_fee = fees
    answer = []
    for car_num, time in sorted(total_time.items()):
        fee = base_fee
        if time > base_time:
            fee += ceil((time - base_time) / unit_time) * unit_fee
        answer.append(fee)

    return answer