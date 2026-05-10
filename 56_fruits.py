def solution(k,m,score):
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
