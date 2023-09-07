def solution(num, total):
    answer = []
    # 연속된 수 num 개의 합은 total -> middle(중간값)은 total을 num으로 나눈 몫
    # middle 기준, 좌우로 값 조정하여 연속된 정수 생성
    middle = total // num
    
    
    # num이 홀수일 때와 짝수일 때
    # 중심값 기준, 좌우로 num/2 만큼 정수를 조합 -> 연속된 정수의 합 만들기
    # 짝수
    if num % 2 == 0: 
        start = middle - num // 2 + 1
    # 홀수
    else: 
        start = middle - num // 2
        
    # 연속된 수 num 개의 정수를 구해서 answer 배열에 추가
    for i in range(start, start + num):
        answer.append(i)
    return answer
