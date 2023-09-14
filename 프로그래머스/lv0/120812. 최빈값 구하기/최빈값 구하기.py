def solution(array):
    array.sort()
    max_count = 0
    current_count = 1
    mode = array[0]
    multiple_mode = False

    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                mode = array[i-1]
                multiple_mode = False
            elif current_count == max_count:
                multiple_mode = True

            current_count = 1

    if current_count > max_count:
        mode = array[-1]
        multiple_mode = False
    elif current_count == max_count:
        multiple_mode = True
    
    return -1 if multiple_mode else mode