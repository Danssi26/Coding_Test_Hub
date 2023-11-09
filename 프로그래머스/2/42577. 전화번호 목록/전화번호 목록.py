def solution(phone_book):
    phone_book.sort()  # 전화번호부를 사전순으로 정렬
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False  # 한 전화번호가 다른 전화번호의 접두어인 경우 False 반환
    
    return True  # 모든 전화번호가 접두어 관계가 아닌 경우 True 반환