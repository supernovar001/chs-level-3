# teacher's solution
def solution(n, m, section):
    count = 0
    current_position = 0
    for s in section :
        if s > current_position : 
            count += 1
            current_position = s + m - 1
    return count

print(solution(8,4,[2,3,6]))#2
print(solution(5,4,[1,3]))#1
print(solution(4,1,[1,2,3,4]))#4

''' 
# my solution
def solution(n, m, section):
    if n == m :
        return 1
    
    # 위치 만들기
    cnt = 0
    start_index  = section[0]  #start_index    
    end_index = start_index 
    
    while start_index <= section[-1] :
        end_index += m  
        start_index = max(end_index, section[cnt])
        cnt += 1
    return cnt
'''
