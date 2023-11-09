from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    for c in course:
        menu_count = defaultdict(int)
        
        for order in orders:
            for combination in combinations(sorted(order), c):
                menu_count["".join(combination)] += 1

        # 가장 많이 주문된 조합 찾기
        sorted_menus = sorted(menu_count.items(), key=lambda x: x[1], reverse=True)

        for menu, count in sorted_menus:
            if count > 1 and count == sorted_menus[0][1]:
                answer.append(menu)

    return sorted(answer)