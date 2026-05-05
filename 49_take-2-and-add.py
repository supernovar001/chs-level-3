def solution(numbers):
    result = []
    for i in range(0,len(numbers)-1):
        for j in range(i+1, len(numbers)):    
            two_add = numbers[i]+numbers[j]
            #print(two_add)
            result.append(two_add)
    sorted(result)
    print(list(set(result)))
    return list(set(result))


# i 0 
# j 1 2 3 4
### 3 5 6 7 

# i 1 
# j 2 3 4
# ## 4 5 2 

# i 2 
# j 3 4
#### 
#  command + ? 주석 단축키 hot key?