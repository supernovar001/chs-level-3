def solution(k,m,score):
<<<<<<< HEAD
    # 1. k indexing [OK]
    #score_modified = sorted(score, reverse = True)
    score.sort(reverse = True)
    score_modified = [ x for x in score if x <= k]
    print(f"score_modified : {score_modified}")
    
    # 2. sublist for m elements ***
    boxes = len(score_modified)//m
    sub_box = []
    print(f"boxes : {boxes}")
    for i in range(0, m*boxes, m):
        sub_box.append((score_modified[i:(i+m)]))
    #print(sub_box, end=" ")
    
    # 3. return outfit
    outfit = []
    for i in range(boxes):
        outfit.append(min(sub_box[i])*m)
        print(f"outfit : {outfit}")
    return sum(outfit)

print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))	#8
print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))	#33))
=======
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
>>>>>>> 6ba9101ebcf000990d047509989cff3be8a377a9
