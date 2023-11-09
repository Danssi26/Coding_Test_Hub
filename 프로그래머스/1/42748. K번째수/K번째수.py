def solution(array, commands):
    answer = []
    
    for cmd in commands:
        i, j, k = cmd
        subarray = array[i - 1:j]  # i번째부터 j번째까지 자르기
        subarray.sort()  # 자른 배열 정렬
        answer.append(subarray[k - 1])  # k번째 숫자 결과 배열에 추가
    
    return answer