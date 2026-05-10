def solution(answers):
<<<<<<< HEAD
    sc1 = [1 ,2, 3, 4, 5]
    sc2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sc3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [ 0, 0, 0 ] ###
    for i in range(len(answers)) :
        if answers[i] == sc1[i % len(sc1)]:
            score[0]+= 1
        if answers[i] == sc2[i % len(sc2)]:
            score[1] += 1
        if answers[i] == sc3[i % len(sc3)]:
            score[2] += 1
    # find the maximum score
    max_score = max(score)
       
    # get the students who have the maximum score
    result = [i+1 for i, x in enumerate(score) if x == max_score]
   # result = [i+1 for i, score in enumerate(score)]
    return result

print(solution([1,2,3,4,5]))    # output : [1]
print(solution([1,3,2,4,2]))    # output : [1,2,3]
=======
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
>>>>>>> 6ba9101ebcf000990d047509989cff3be8a377a9
