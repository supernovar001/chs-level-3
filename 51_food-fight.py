def solution(s):
    arrangement = ''
    for i in range(1, len(s)) :
        count = s[i]//2
        arrangement += str(i) * count
    final_arrangement = arrangement + '0' + arrangement[::-1]
    return final_arrangement

print(solution([1, 3, 4, 6]))