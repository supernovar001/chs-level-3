def solution(s, n):
    result = ''
    for char in s :
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            #print(f"Processing Character : {char}, ASCII offset : {ascii_offset}")
            shifted =(ord(char) - ascii_offset + n) % 26 + ascii_offset
            #print(f"Original ASCII : {ord(char)}, Shifted ASCII : {shifted}")
            result +=chr(shifted)
        
        else : 
            result +=char # 공백
    return result