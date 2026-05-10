def solution(a, b):
    # 월별 일수만 담긴 리스트
    monthday_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayofweek_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    
    # a월 b일은 2016년의 몇번째 날인가요?
    day_ab = sum(monthday_list[0:a])+b-1    #1월1일 = 0
    print(day_ab) #145가 나와야함
    return dayofweek_list[(5+day_ab)%7]

print(solution(5,24))   # "TUE"