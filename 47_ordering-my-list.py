def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(["sun", "bed", "car"],1))
 
'''
    sorted_answer = strings.sort(key = lambda x : x[n])
    print(sorted_answer)
    return sorted_answer
    '''


'''
💡 한 줄 요약
sort()는 반환값 없음 → 원본 수정
sorted()는 새 리스트 반환
이 문제는 (x[n], x) 튜플 정렬이 핵심'''


