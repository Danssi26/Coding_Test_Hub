def solution(record):
    # 유저 아이디와 닉네임을 저장하는 딕셔너리
    user_info = {}
    # 결과 메시지를 저장할 리스트
    result = []
    
    # 1번 작업: 각 사용자의 최종 닉네임 추적
    for r in record:
        split_r = r.split()
        action = split_r[0]
        
        # Enter 혹은 Change 액션인 경우에 닉네임을 업데이트함
        if action == "Enter" or action == "Change":
            user_id = split_r[1]
            nickname = split_r[2]
            user_info[user_id] = nickname
    
    # 2번 작업: 메시지 생성
    for r in record:
        split_r = r.split()
        action = split_r[0]
        user_id = split_r[1]
        
        if action == "Enter":
            result.append(user_info[user_id] + "님이 들어왔습니다.")
        elif action == "Leave":
            result.append(user_info[user_id] + "님이 나갔습니다.")
    
    return result
