def solution(s) :
    # s를 리스트로 변환 (분리 기준 : 단어, 공백(' '))    
    s = list(s.split(' '))     # s : ['try', 'hello', 'world']
    
    z = []
    # list의 element에 접근하는 loop
    for x in s :    
        result = ''     # 빈 문자열 선언하는 이유 : 문자열의 값을 변경할 수 없음

        # list의 element(문자열)의 각 한글자씩 접근하는 loop
        # 한글자씩 대소문자 변경한 값을 빈 문자열이었던 result에 한개씩 추가
        for i in range(len(x)):
            if i % 2 == 0:
                result += x[i].upper()
            else :
                result += x[i].lower()

        z.append(result)
    return ' '.join(z)

print(solution('try hello world'))  