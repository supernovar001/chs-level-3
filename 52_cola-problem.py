def solution( a , b , n) :
# a : 빈병 a개를 주면 새 콜라 b병을 주는 
    count = 0
    while n >= a :  
    #  a # cal_empty_cola
    #  b # cal_new_cola
    #  n # empty_cola
    # return 상빈이가 받을 수 있는 콜라 수 

    #1. 받을 수 있는 콜라 공식 : 
    # 교환할 빈 콜라 병 수= (n//a)
        return_cola = (n // a) * b
        n = return_cola + n % a
        count += return_cola
    return count 

print(solution(2,1,20))
print(solution(3,1,20))