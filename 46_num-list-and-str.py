def solution(s):
    numberdict =  {"zero" : "0", 
                "one" : "1",
                "two" : "2",
                "three" : "3",
                "four" : "4",
                "five" : "5",
                "six" : "6",
                "seven" : "7",
                "eight" : "8",
                "nine": "9"}
    '''
    for key in numberdict.keys() :
        s = s.replace(key, numberdict[key])
    '''    
    for key, value in numberdict.items():
        s = s.replace(key, value)
        #print(s)
    return int(s)