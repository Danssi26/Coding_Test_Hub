def solution(array):
    # 배열에서 각 숫자 빈도 세기
    # 빈 딕셔너리 생성, 숫자 빈도 저장
    num_counts = {}
    
    # 배열 순회, 각 숫자 빈도 업데이트
    for num in array:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    
    # 빈도가 가장 높은 값
    max_count = max(num_counts.values())
    
    # 빈도가 가장 높은 '값들'
    answer = [num for num, count in num_counts.items() if count == max_count]
    
    # 최빈값이 여러 개면 -1 return
    if len(answer) > 1:
        return -1
    else:
        return answer[0]