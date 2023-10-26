import heapq

# 시간-분 변환 함수
def convert(time_str): 
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


def solution(book_time):

    converted_times = [(convert(start), convert(end) + 10) for start, end in book_time]    
    converted_times.sort(key=lambda x: x[0])
    
    rooms = []  #힙
    for start, end in converted_times:
        # 사용 가능한 객실이 있으면 
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)  # 그 객실의 종료 시간을 힙에서 제거
        heapq.heappush(rooms, end)  # 새로운 객실의 종료 시간을 힙에 추가
    
    return len(rooms)