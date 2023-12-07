def solution(keymap, targets):
    char_to_key = {}
    for key, chars in enumerate(keymap, start=1):
        for i, char in enumerate(chars, start=1):
            if char not in char_to_key:
                char_to_key[char] = []
            char_to_key[char].append((key, i))

    answer = []
    
    for target in targets:
        key_presses = 0
        for char in target:
            if char in char_to_key:
                key_presses += min([press for _, press in char_to_key[char]])
            else:
                key_presses = -1
                break
        answer.append(key_presses)

    return answer

