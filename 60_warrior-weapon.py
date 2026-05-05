# 58 60 암기
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
    maxpower = count_divisors(number)
    if maxpower > limit :
        maxpower = power
    return maxpower

print(solution[5,3,2])#10
print(solution[10,3,2])#21

