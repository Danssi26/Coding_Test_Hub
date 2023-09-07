def solution(num, total):
    answer = []
    # 연속된 num 개의 정수의 합이 total이 되도록 가운데 값이 total을 num으로 나눈 몫으로
    middle = total // num
    
    # num이 홀수일 때와 짝수일 때를 나누어 처리
    # 짝수일 경우
    if num % 2 == 0: 
        start = middle - num // 2 + 1
    # 홀수일 경우    
    else: 
        start = middle - num // 2
        
    # 연속된 num 개의 정수를 구해서 answer 배열에 추가
    for i in range(start, start + num):
        answer.append(i)
    return answer