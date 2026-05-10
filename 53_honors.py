def solution(k, score):
    answer = []
    score_list_i = []
    for i in range(1, len(score)+1):
        score_list_i = sorted(score[0:i],reverse=True)[0:k]
        # print(f"{i}:{score_list_i}")
        answer.append(min(score_list_i[0:k])) #상위 3개만 출력 중에서 최하위
    # print(f"answer : {answer}, score_list_i:{score_list_i}")
    return answer

# print(solution(3,[10, 100, 20, 150, 1, 100, 200]))
# [10, 10, 10, 20, 20, 100, 100]

# print(solution(3,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
# 정답    [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
# 내 출력 [0, 0, 0, 40, 40, 70, 150, 150, 300, 300]