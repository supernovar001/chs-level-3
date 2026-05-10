<<<<<<< HEAD
def solution(lottos, win_nums):
	
    rank = [6,6,5,4,3,2,1]
    matched = sum(1 for num in lottos if num in win_nums)
    unknowns =lottos.count(0)
    return [rank[matched+ unknowns], rank[matched]]
print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))  #[3,5]
'''

def solution(lottos, win_nums):
    cnt = 0
    for x in win_nums :
        if x in lottos :    #?????????????
            cnt +=1
            
    zero_count = lottos.count(0)
    max_count = cnt + zero_count
=======


def solution(lottos, win_nums):
    cnt = 0

    #  로또 당첨번호 vs 제출한 번호 중에서 동일한 element가 있을 때마다 cnt+=1 하는 목적의 반복문
    for x in win_nums :
        if x in lottos :    #?????????????
            cnt +=1

    # 최종적으로 얻은 cnt로 max_count, min_count를 구한다.
    zero_count = lottos.count(0)
    max_count = cnt + zero_count	# '0'
>>>>>>> 6ba9101ebcf000990d047509989cff3be8a377a9
    min_count = cnt
    print(f"max_count:{max_count},min_count:{min_count}, zero_count:{zero_count}")
    result = [rank_count(max_count), rank_count(min_count)]
    return result    

def rank_count(cnt):
<<<<<<< HEAD
=======
	# 로또 당첨번호 vs 제출한 번호 중에서 동일한 것이 있을 때마다 cnt+=1 
>>>>>>> 6ba9101ebcf000990d047509989cff3be8a377a9
	if cnt <= 1 :
		return 6
	elif cnt == 2 :
		return 5
	elif cnt == 3 :
		return 4
	elif cnt == 4 :
		return 3
	elif cnt == 5 :
		return 2
	else :
<<<<<<< HEAD
		return 1
		
'''
=======
		return 1
>>>>>>> 6ba9101ebcf000990d047509989cff3be8a377a9
