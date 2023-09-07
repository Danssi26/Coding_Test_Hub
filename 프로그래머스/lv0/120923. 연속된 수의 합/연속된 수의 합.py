def solution(num, total):
    answer = []
    # 연속된 수 num 개의 합은 total -> middle은 total을 num으로 나눈 몫
    middle = total // num
    
    # num이 홀수일 때와 짝수일 때
    # 짝수
    if num % 2 == 0: 
        start = middle - num // 2 + 1
    # 홀수
    else: 
        start = middle - num // 2
        
    # 연속된 num 개의 정수를 구해서 answer 배열에 추가
    for i in range(start, start + num):
        answer.append(i)
    return answer