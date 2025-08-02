#화폐 간의 관계가 서로 배수 관계 -> 그리디 가능
def solution(amount):
    denominations = [100,50,10,1]
    change = []
    for coin in denominations:
        #현재 화폐 단위로 최대한 거슬러 줄 수 있는 동전의 갯수 구함
        count = amount // coin
        change.extend([coin] * count)
        #정산이 완료된 거스름돈 제외
        amount %= coin
        
    return change

print(solution(450))