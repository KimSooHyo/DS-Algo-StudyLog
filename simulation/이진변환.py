def solution(s):
    #이진 변환 횟수 저장하는 변수
    count_transform = 0
    #제거된 0의 개수 저장하는 변수
    count_zero = 0
    
    #s가 1이 아닌 동안 계속 반복
    while s != '1':
        #이진 변환 횟수 1 증가
        count_transform += 1
        #s에서 '0'의 개수 세어 count_zero에 누적
        count_zero += s.count("0")
        #s에서 1의 개수를 세고, 이를 이진수로 변환
        #bin() 함수 사용하기 위해 0b 뒤의 문자열 활용
        s = bin(s.count("1"))[2:]
        
    #이진 변환 횟수와 제거된 모든 0의 개수를 리스트에 담아 반환
    return [count_transform, count_zero]