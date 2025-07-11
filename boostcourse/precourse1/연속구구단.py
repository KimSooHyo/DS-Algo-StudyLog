n = 1

while(n != 0):
    print("구구단 몇 단을 계산할까요?(1~9)")
    n = int(input())
    if n > 9:
        continue
    print("구구단 5단을 계산합니다.")
    for i in range(1, 10):
        print(f"{n} X {i} = {n*i}")
        
print("구구단 게임을 종료합니다.")