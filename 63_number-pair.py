def solution(x,y):
    result = ''
    for i in range(len(x)) :
        for j in range(len(y)) :
            if x[i] == y[j] :
                result += x[i]
    print(result)
    list_result = list(result)
    list_result.sort(reverse = True)
    return ''.join(list_result)

print(solution("12321","42531")) #321
print(solution("100","203045")) #0
