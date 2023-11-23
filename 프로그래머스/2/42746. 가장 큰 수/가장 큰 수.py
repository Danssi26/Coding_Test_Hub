def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers = [str(number) for number in numbers]

    # 숫자 정렬(내림차순)
    numbers.sort(key=lambda x: x*3, reverse=True)

    # 가장 큰 숫자가 '0'인 경우 결과는 '0'
    if numbers[0] == "0":
        return "0"

    # 정렬된 숫자들을 하나의 문자열로 결합
    return ''.join(numbers)

