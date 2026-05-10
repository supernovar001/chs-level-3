def solution(food):
    left_result = ''
    count = 0
    for i in range(1, len(food)):
        count = (food[i]//2)
        #print(count)
        left_result += str(i) * count
    
    result = left_result + '0' + left_result[::-1]
    return result

print(solution([1, 3, 4, 6]))