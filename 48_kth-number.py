def solution(array, commands):
    answer = []
    for i, j, k in commands : #commands[0],commands[1],commands[2]
        # sorting
        pick = (array[i-1:j])
        sorted_pick = sorted(array[i-1:j])
        answer.append(sorted_pick[k-1]) 
    return answer
    
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])) #[5,6,3]