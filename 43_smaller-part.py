def solution(t, p):
    cnt = 0
    for idx in range(0,len(t)-len(p)+1,1):  # 범위 설정 주의      
        x = t[idx:idx+len(p)]
        # print(x)
        if int(p) >= int(x):
            cnt += 1
            
    return cnt

print(solution("3141592","271")) #result : 2
print(solution("500220839878","7")) #result : 8
print(solution("10203","15")) #result : 3