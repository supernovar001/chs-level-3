def solution(answers):
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
