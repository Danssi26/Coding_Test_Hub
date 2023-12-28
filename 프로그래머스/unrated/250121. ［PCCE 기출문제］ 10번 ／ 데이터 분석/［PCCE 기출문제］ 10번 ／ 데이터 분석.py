# data 기준 20300501 이전 데이터 필터링
# remain을 기준으로 오름차순 정렬

def solution(data, ext, val_ext, sort_by):

    # 열 이름 사용하여 데이터에서 해당 열 찾기
    # 각 열의 이름과 해당 인덱스 mapping dic 생성  
    mapping = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    # data에서 항목 순회, ext 열 값이 val_ext 보다 작은 항목만 선택하고 list 생성
    filtered_data = []
    for item in data:
        if item[mapping[ext]] < val_ext:
            filtered_data.append(item)
# list comprehension
# filtered_data = [item for item in data if item[column_mapping[ext]] < val_ext]

    # 오름차순 정렬
    sorted_data = sorted(filtered_data, key=lambda x: x[mapping[sort_by]])

    return sorted_data