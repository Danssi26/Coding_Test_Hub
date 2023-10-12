def can_make_word(word, sounds):
    if not word:  
        return True
    
    for sound in sounds:
        if word.startswith(sound): 
            if can_make_word(word[len(sound):], [s for s in sounds if s != sound]):
                return True
            
    return False  

def solution(babbling):
    possible_sounds = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        if can_make_word(word, possible_sounds): 
            answer += 1

    return answer
