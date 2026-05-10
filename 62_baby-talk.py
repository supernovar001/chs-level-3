def solution(babbling):
    # Define the possible words that the baby can pronounce
    possible_words = ['aya', 'ye', 'woo', 'ma']
    # initialize a counter for valid words
    count = 0
    # iterate through each word in the input list
    for word in babbling :
        original_word = word    # store the original word for reference !!! 
        # 내용 변형이 있어서 원본 복원 차원에서 original_word를 새로 선언함
        # Replace the possible words in the word with a place holder ' '
        for pw in possible_words :
            word = word.replace(pw, ' ')
        
        # Check if the modified word consists only of spaces
        # (valid pronounciation)
        if word.strip() == "":
            # Check for consecutive same words using simple logic
            is_valid = True
            for pw in possible_words:
                if pw*2 in original_word :
                    is_valid = False
                    break
            if is_valid :
                count += 1
    return count
print(solution(["aya", "yee", "u", "maa"])) # output : 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])) #output : 2