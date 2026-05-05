# 약수의 개수
def count_divisors(num):
    count = 0
    for i in range(1, int(num)**0.5 + 1):
        if num % i == 0 :
            count +=1
            if i != num // i :
                count += 1
    return count

def solution(number, limit, power):
    power = count_divisors(number)
    if power > limit :
        power = limit
    return power