def solution(answers):
    sc1 , sc2, sc3 = [] , [], []
    ss1 = [1, 2, 3, 4, 5]
    ss2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ss3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 1부터 시작하는 인덱스
    for idx, student_score in enumerate(ss1):
        sc1.append(student_score)
        print(sc1)
    for idx, student_score in enumerate(ss2):
        sc2.append(student_score)
    for idx, student_score in enumerate(ss3):
        sc3.append(student_score)   
    print(sc1)
    print(sc2)
    print(sc3)


print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2]))	# [1,2,3]