def solution(card1, card2, goal):
    for i in range(len(goal)) : 
        for j in range(card1):
            if card1[j] == i :
                continue
            else : 
                return "No"
        for k in range(card2):
            if card2[k] == i :
                continue
            else : 
                return "No"
    return "Yes"
print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))	#  "Yes"
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))	#  "No"