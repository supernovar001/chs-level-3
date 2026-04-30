def solution(s):
    # 문자열 리스트 변환 시 공백을 기준으로 스플릿 필요
    a = list(s.split())
    for x in a :
        for idx in range(len(x)) :
            if idx %2 == 0 :
                a[idx] = a[idx].upper()
            else : 
                a[idx] = a[idx].lower()
    return a