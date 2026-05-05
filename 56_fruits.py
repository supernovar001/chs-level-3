def solution(k,m,score):
    packable_box = len(score)//m
    unpackable = len(score) % m
    
    if unpackable == 0 :
        packable_list = sorted(score, reverse =True)
    else :
        packable_list = sorted(score, reverse = True)[:-unpackable]
        
    score_not_greater_k = [x for x in score if x <= k]
    sum_score = 0
    for i in range(packable_box) :
        box = packable_list[i*m: (i+1)*m]
        sum_score += m * min(box)
    return sum_score