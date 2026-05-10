# 약수의 개수
def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0 :
            count +=1
            #print(i, end = " ")

            # 완전제곱수에서 중복되는 중앙 약수를 한번만 세기 위함
            # i가 약수이면 num // i 도 약수
            if i != (num // i) :
                count += 1
    return count

def solution(number, limit, power):
    total_weight = 0 
    for i in range(1, number+1):
        attack_power = count_divisors(i)
        if attack_power > limit :
            attack_power = power
        total_weight += attack_power
    return total_weight

print(solution(5,3,2))#10