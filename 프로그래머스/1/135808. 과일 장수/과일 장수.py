
# 최대한 많은 상자에 사과를 담아 판매할 때 얻을 수 있는 이익을 계산하는 것을 목표 
# 각 상자에는 최대 m개의 사과를 담을 수 있음. 상자의 가치는 그 안에 들어 있는 사과 중 가장 낮은 점수를 가진 사과의 점수와 같음

def solution(k, m, score):
    # 사과 점수를 오름차순으로 정렬
    score.sort()

    # 최대 이익 계산
    max_profit = 0
    # 상자에 담길 사과 개수만큼 반복하며, 뒤에서부터 m개씩 상자를 만듦
    for i in range(len(score) - m, -1, -m):
        # 상자에 담긴 사과 중 최소 점수
        min_score_in_box = score[i]
        # 상자 가치를 최대 이익에 더함
        max_profit += min_score_in_box * m

    return max_profit
