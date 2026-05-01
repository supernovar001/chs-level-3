def solution(t, p):
    cnt = 0
    for idx in range(0,len(t)-len(p)+1,1):
        
        x = t[idx:idx+len(p)]
        print(x)
        if int(p) >= int(x):
            cnt += 1
            
    return cnt

print(solution("33124141592","2721")) #result == 2