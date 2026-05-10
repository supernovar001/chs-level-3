def solution(X,Y):
    # 숫자 개수 저장용 딕셔너리 생성
    count_X = {}
    count_Y = {}
    
    # counting each digit in X, Y 
    for digit in X :
        if digit in count_X:
            count_X[digit] +=1
        else :
            count_X[digit] = 1

    for digit in Y:
        if digit in count_Y:
            count_Y[digit] +=1
        else :
            count_Y[digit] =1

    common_digit = []
    for digit in count_X :
        if digit in count_Y:
            common_digit.extend([digit]*min(count_X[digit], count_Y[digit]))
    
    # print(X)
    # print(Y)

    if not common_digit:
        return "-1"
    
    # if the largest number is "0" .. return "0"
    common_digit.sort(reverse=True)
    if common_digit[0] == "0":
        return "0"
    
    # j9oin and return as a string
    return "".join(common_digit)

print(solution("100", "2345"))     # -1
print(solution("100", "203045"))   # 0
print(solution("100", "123450"))   # 10
print(solution("12321", "42531"))  # 321
print(solution("5525", "1255"))    # 552