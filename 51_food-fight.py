<<<<<<< HEAD
def solution(food):
    left_result = ''
    count = 0
    for i in range(1, len(food)):
        count = (food[i]//2)
        #print(count)
        left_result += str(i) * count
    
    result = left_result + '0' + left_result[::-1]
    return result
=======
def solution(s):
    arrangement = ''
    for i in range(1, len(s)) :
        count = s[i]//2
        arrangement += str(i) * count
    final_arrangement = arrangement + '0' + arrangement[::-1]
    return final_arrangement
>>>>>>> 6ba9101ebcf000990d047509989cff3be8a377a9

print(solution([1, 3, 4, 6]))