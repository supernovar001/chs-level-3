def solution(babbling):
    # Define the possible words that the baby can pronounce
    possible_words = ['aya', 'ye', 'woo', 'ma']
    # initialize a counter for valid words
    count = 0
    # iterate through each word in the input list
    for word in babbling :
        original_word = word    # store the original word for reference
        # Replace the possible words in the word with a place holder ' '
        for idx, pw in enumerate(possible_words) :
            word = word.replace(pw, str(idx+1))
            # 'aya' → '1', 'ye' → '2', 'woo' → '3', 'ma' → '4'

        # Check for consecutive same words using simple logic
        # 변환된 word가 만약 '112'라면, word[0]과 word[1]이 모두 '1'(aya)이므로 invalid를 True로 설정하고 검사를 중단합니다.
        invalid = False
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                invalid = True
                break
        # if no invalid repetition and all letters replaced, it's prononceable if not invalid and word.isdigit():
        if not invalid and word.isdigit():  
            count += 1
            #  not invalid: 앞서 체크한 연속된 발음이 없어야 합니다.
            # word.isdigit(): 만약 아기가 발음할 수 없는 글자(예: 'u', 'a')가 섞여 있다면 숫자로 바뀌지 않고 문자로 남아있게 됩니다. 즉, 모든 글자가 숫자로 바뀌었는지를 확인하여 완벽하게 발음 가능한 단어인지 판별합니다.
    return count
print(solution(["aya", "yee", "u", "maa"])) # output : 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])) #output : 2
