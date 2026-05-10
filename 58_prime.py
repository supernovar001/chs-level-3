<<<<<<< HEAD
def is_prime(n):
    # "check if a number is prime"
    if n < 2 : 
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    num = 0
    cnt = 0
    # 3. list 내 3개의 수를 더하는 방법
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                if is_prime(num) == True : # 소수인지 확인하는 function 사용
                    cnt +=1 
        
    return cnt

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
=======
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
>>>>>>> 6ba9101ebcf000990d047509989cff3be8a377a9
