def solution(number):
    count = 0
    n = len(number)

    for i in range(n - 2):  # First student
        #print(f'i: {i}')
        for j in range(i + 1, n - 1):  # Second student
            #print(f'j: {j}')
            for k in range(j + 1, n):  # Third student
             #   print(f'k: {k}')
                if number[i] + number[j] + number[k] == 0:
                    count += 1

    return count
print(solution([-2, 3, 0, 2, -5]))          # Output : 2
print(solution([-3, -2, -1, 0, 1, 2, 3]))   # Output : 5
print(solution([-1, 1, -1, 1]))             # Output : 0

