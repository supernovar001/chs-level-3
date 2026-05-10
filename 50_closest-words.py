# helper function
def find_previous_occurrence(index, s):
    #0, banana  # 1, banana   #2, banana
    for j in range(index - 1, -1, -1):
        print(f'current location: {index}, location j: {j}, s[j]: {s[j]}, s[index]: {s[index]}  ')
        # -1, 
        if s[j] == s[index]:
            return index - j 
    return -1
    #return : 현재 문자와 같은 문자가 바로 이전에 등장한 위치까지의 거리 (없다면 -1)
    print(s)

def solution(s):
    answer = []
    for i in range(len(s)):
        answer.append(find_previous_occurrence(i, s))
    return answer
'''
"banana"	[-1, -1, -1, 2, 2, 2]
"foobar"	[-1, -1, 1, -1, -1, -1]
'''
print(solution("banana"))
print(solution("footbar"))

