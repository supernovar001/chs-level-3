def solution(n, lost,reserve):
    answer = 0
    lost_set = set(lost)-set(reserve)
    reserve_set = set(reserve)-set(lost)

    for student in sorted(reserve_set):

    # 앞 번호 학생에게 빌려주기
        if student-1 in lost_set :
            lost_set.remove(student-1)
        # 뒷번호 학생에게 빌려주기
        elif student+1 in lost_set :
            lost_set.remove(student+1)

    return n - len(lost_set)
print(solution(5, [2,4],[1,3,5])) #5
print(solution(5, [2,4],[3])) #4
print(solution(3, [3],[1])) #2
