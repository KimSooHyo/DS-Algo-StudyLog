def solution(want, number, discount):
    want_dict = {} #구매하려는 제품은 키, 개수는 값
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    answer = 0 #만족하는 일수를 저장하는 변수
    
    #특정 일이 모든 제품을 할인받을 수 있는 지 확인
    for i in range(len(discount) - 9):
        discount_10d = {} #회원가입 시 할인받는 제품 및 개수를 담은 딕셔너리
        
        #i일 회원가입 시 할인 받는 제품 및 개수로 딕셔너리 구성
        for j in range(i, i + 10):
            if discount[j] in want_dict:
                discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1
                
        #i일에 구매하려는 모든 제품을 할인 받는다면 answer 증가
        if discount_10d == want_dict:
            answer += 1
            
    return answer